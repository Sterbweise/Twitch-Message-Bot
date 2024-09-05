import asyncio
import configparser
import requests
from twitchio.ext import commands
import random

# Read configuration from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract Twitch credentials from config
ACCESS_TOKEN = config['Twitch']['access_token']
REFRESH_TOKEN = config['Twitch']['refresh_token']
CLIENT_ID = config['Twitch']['client_id']
CHANNELS = config['Twitch']['channels'].split(',')

def refresh_access_token():
    url = 'https://id.twitch.tv/oauth2/token'
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN,
        'client_id': CLIENT_ID
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['access_token']
    else:
        print(f"Error while refreshing token: {response.status_code}")
        return None

class TwitchBot(commands.Bot):
    def __init__(self):
        # Initialize the bot with Twitch credentials
        self.access_token = ACCESS_TOKEN
        super().__init__(token=f'oauth:{self.access_token}', prefix='!', initial_channels=CHANNELS)
        self.message_interval = int(config['Bot']['message_interval'])
        self.messages = config['Bot']['messages'].split('|')
        
        # Store channels for easy access
        self.channels = CHANNELS

    async def event_ready(self):
        # Called once when the bot goes online
        print(f'Logged in as | {self.nick}')
        # Start the periodic message sending task
        self.loop.create_task(self.send_periodic_messages())

    async def send_periodic_messages(self):
        while True:
            # Choose a random message from the list
            message = random.choice(self.messages)
            
            # Send the message to all channels
            for channel_name in self.channels:
                channel = self.get_channel(channel_name)
                if channel:
                    await channel.send(message)
                    print(f"Message sent to {channel_name}: {message}")
                else:
                    print(f"Unable to find channel: {channel_name}")
                await asyncio.sleep(1)  # Small delay between each send to avoid rate limiting
            
            print(f"Waiting {self.message_interval} seconds before the next sending cycle.")
            await asyncio.sleep(self.message_interval)

bot = TwitchBot()
bot.run()
