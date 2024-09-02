# Ditify

Ditify is a lightweight Python script designed to receive notifications intended for Gotify and forward them as direct messages (DMs) to specified users on Discord using a Discord bot. The script can be optionally run inside a Docker container, making deployment simple and straightforward.

It was originally designed for use with the Proxmox notification system. Therefore, if you plan to use it for a different purpose, some adjustments may be necessary.

## Features

- **Message Forwarding**: Forwards Gotify notifications as Discord DMs to specified users.
- **Configurable via JSON**: Easily set up and manage tokens and user IDs via `config.json`.
- **Docker Support**: Deploy Ditify using Docker with a provided `Dockerfile` and `docker-compose.yml` configuration.

## Prerequisites

- Python 3.9+ or Docker
- A Discord bot token
- Docker (optional, if running in a container)

## Setting Up a Discord Bot

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application.
3. Under the "OAuth2" section, ensure "User Install" is selected and copy the installation link.
4. Open a new tab, paste the link, and follow the instructions to authorize the bot.
5. Return to the Discord panel, navigate to the "Bot" settings, and reset your token. Be sure to copy the token—you'll need it later during the Ditify setup.

## Running Manually

### 1. Clone the Repository

```
git clone https://github.com/yourusername/ditify.git
cd ditify
```

### 2. Configure the `config.json`

Copy the template file and update it with your Discord bot token, user IDs, and Gotify tokens.

```
cp config.json.template config.json
```

Edit `config.json` to your likings.


### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Ditify

```
python main.py
```

## Running with Docker (Docker-Compose)

### 1. Clone the Repository

```
git clone https://github.com/yourusername/ditify.git
cd ditify
```

### 2. Configure the `config.json`

Copy the template file and update it with your Discord bot token, user IDs, and Gotify tokens.

```
cp config.json.template config.json
```

Edit `config.json` to your likings.

### 3. Run the Container with Docker Compose

Run:

```
docker-compose up -d
```

The application will be accessible and ready to receive Gotify notifications at `http://localhost:5000/message`.

## Usage

Once Ditify is running, it will listen for incoming messages sent to the `/message` endpoint. These messages must include a valid token in either the `Authorization` header or as a query parameter. Upon receiving a valid message, Ditify forwards it to the specified Discord users.

## Example Request

Here's an example of a `POST` request to send a message:

```
curl -X POST http://localhost:5000/message \
-H "Authorization: Bearer yourgotifytoken" \
-H "Content-Type: application/json" \
-d '{"title": "Test Notification", "message": "This is a test message"}'
```
or
```
curl -X POST http://localhost:5000/message?token=yourgotifytoken \
-H "Content-Type: application/json" \
-d '{"title": "Test Notification", "message": "This is a test message"}'
```

## Troubleshooting

- Ensure the Discord bot is properly configured and has permission to send DMs, also that you addet at to your bots.
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
