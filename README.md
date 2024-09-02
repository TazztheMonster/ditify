# Ditify

Ditify is a lightweight Python script designed to receive notifications intended for Gotify and forward them as direct messages (DMs) to specified users on Discord using a Discord bot. The script can be optionally run inside a Docker container, making deployment simple and straightforward.

## Features

- **Message Forwarding**: Forwards Gotify notifications as Discord DMs to specified users.
- **Discord Bot Integration**: Uses a Discord bot to send messages directly to users.
- **Configurable via JSON**: Easily set up and manage tokens and user IDs via `config.json`.
- **Docker Support**: Deploy Ditify using Docker with a provided `Dockerfile` and `docker-compose.yml` configuration.

## Prerequisites

- Python 3.9+
- A Discord bot token
- Docker (optional, if running in a container)

## Installation

### 1. Clone the Repository

'''
git clone https://github.com/yourusername/ditify.git
cd ditify
'''

### 2. Configure the `config.json`

Copy the template file and update it with your Discord bot token, user IDs, and Gotify tokens.

'''
cp config.json.template config.json
'''

Edit `config.json`:

'''
{
  "discord_token": "YourDiscordBotToken",
  "user_ids": [
    123456789012345678
  ],
  "tokens": [
    {
      "name": "ExampleToken",
      "token": "yourgotifytoken"
    },
    {
      "name": "OtherExample",
      "token": "anothergotifytoken"
    }
  ]
}
'''

### 3. Install Dependencies

'''
pip install -r requirements.txt
'''

### 4. Run Ditify

'''
python main.py
'''

## Running with Docker

### 1. Run the Container with Docker Compose

Simply run:

'''
docker-compose up -d
'''

The application will be accessible and ready to receive Gotify notifications at `http://localhost:5000/message`.

## Usage

Once Ditify is running, it will listen for incoming messages sent to the `/message` endpoint. These messages must include a valid token in either the `Authorization` header or as a query parameter. Upon receiving a valid message, Ditify forwards it to the specified Discord users.

## Example Request

Here's an example of a `POST` request to send a message:

'''
curl -X POST http://localhost:5000/message \
-H "Authorization: Bearer yourgotifytoken" \
-H "Content-Type: application/json" \
-d '{"title": "Test Notification", "message": "This is a test message"}'
'''

## Troubleshooting

- Ensure the Discord bot is properly configured and has permission to send DMs.
- Check that the `config.json` file is correctly populated with valid tokens and user IDs.
- If running inside Docker, make sure the container is running and accessible.

## Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Gotify](https://gotify.net)
- [Discord.py](https://discordpy.readthedocs.io)
- [ChatGPT](https://chatgpt.com/) for helping me out when im lost.
