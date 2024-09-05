# Twitch Auto-Message Bot

This Twitch bot automatically sends periodic messages to specified Twitch channels. It's designed to help streamers maintain engagement in their chat even during quieter moments.

## Features

- Sends random messages from a predefined list at regular intervals
- Supports multiple Twitch channels simultaneously
- Configurable message interval
- Easy-to-use configuration file for messages and channels
- Utilizes Twitch API for secure authentication

## Prerequisites

- Python 3.7 or higher
- `requests` library
- `twitchio` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/twitch-auto-message-bot.git
   cd twitch-auto-message-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration


1. Edit `config.ini` and fill in the following details:

   ```ini
   [Twitch]
   access_token = your_access_token_here
   refresh_token = your_refresh_token_here
   client_id = your_client_id_here
   channels = channel1,channel2,channel3

   [Bot]
   message_interval = 1200
   messages = Message 1 | Message 2 | Message 3
   ```

   - `access_token`: Your Twitch access token
   - `refresh_token`: Your Twitch refresh token
   - `client_id`: Your Twitch application's client ID
   - `channels`: Comma-separated list of channels the bot should join
   - `message_interval`: Time in seconds between message cycles
   - `messages`: Pipe-separated list of messages the bot will randomly choose from

## Obtaining Twitch Tokens

To get your Twitch tokens:

Use the [Twitch Token Generator](https://twitchtokengenerator.com/) to generate your access and refresh tokens:
   - Select "Custom Scope Token"
   - Check the boxes for `chat:read` and `chat:edit` scopes
   - Click "Generate Token"
   - Authorize the application
   - Copy the generated Access Token, Refresh Token, and Client ID

## Usage

Run the bot using:
```bash
python main.py
```

The bot will automatically:
- Connect to the specified Twitch channels
- Send a random message from your configured list to all channels every 20 minutes

## Customization

- To change the message interval, modify the `self.message_interval` value in `main.py` (default is 1200 seconds or 20 minutes).
- Add or remove messages by editing the `messages` line in `config.ini`.
- Add or remove channels by editing the `channels` line in `config.ini`.

## Important Notes

- This bot uses your personal Twitch account. Ensure you comply with Twitch's Terms of Service and Community Guidelines.
- Do not share your access token, refresh token, or client ID publicly.
- Excessive messaging may lead to timeouts or bans. Use responsibly and respect channel rules.

## Troubleshooting

- If the bot disconnects frequently, ensure your tokens are valid and have the correct scopes.
- If messages aren't sending, check that the bot has the necessary permissions in the target channels.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This bot is not affiliated with or endorsed by Twitch. Use at your own risk.
