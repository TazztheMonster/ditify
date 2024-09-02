import discord
from flask import Flask, request, jsonify
import json
import threading
import logging

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['discord_token']
user_ids = config['user_ids']
valid_tokens = {item['token']: item['name'] for item in config['tokens']}

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def send_dm(user_id, message):
    user = await client.fetch_user(user_id)
    try:
        await user.send(message)
    except discord.Forbidden:
        print(f"Couldn't send a message to {user.name}. The user may have disabled DMs.")

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.split(' ')[1] if 'Bearer' in auth_header else None

    if token is None:
        token = request.headers.get('X-Gotify-Key', request.args.get('token', ''))

    if token in valid_tokens:
        data = request.json
        message = data.get('message', 'No message available.')
        title = data.get('title', 'No Title available')
        token_name = valid_tokens[token]
        full_message = f"# {title}\n{message}\n-# Token Name: {token_name}\n\n\n"

        for user_id in user_ids:
            threading.Thread(target=lambda: client.loop.create_task(send_dm(user_id, full_message))).start()
        return jsonify({"status": "success", "message": "Message has been sent"}), 200
    else:
        app.logger.error(f"Invalid token received: {token}")
        app.logger.error(f"Authorization Header: {auth_header}")
        app.logger.error(f"Request Headers: {request.headers}")
        app.logger.error(f"Request Args: {request.args}")
        app.logger.error(f"Request IP: {request.remote_addr}")
        return jsonify({"status": "error", "message": "Invalid token"}), 403


def run_server():
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

server_thread = threading.Thread(target=run_server)
server_thread.start()

client.run(TOKEN)
