import discord
import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

def get_meme():
  response = requests.get('https://meme-api.com/gimme')   # GET request
  json_data = json.loads(response.text)                   # read the JSON-formatted data
  return json_data['url']

# MyClient class is created by extending from the discord.Client(see discord API), so it will inherit its methods/functions, 
# such as on_ready(), on_message(), on_member__join()
# and this class will be used to interact with Discord API
class MyClient(discord.Client):

  # once Discord bot's login is successful
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # method for bot to read message on the discord channel and respond to them
  async def on_message(self, message):
    # check if the sender is the bot itself
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello World!')

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

  # When a new member joins the discord server, the bot send a welcome message
  async def on_member_join(self, member):
    # define the channel to send the welcome message in
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
      await channel.send(f"Welcome to the server, {member.mention}! 🎉")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN")) # Replace with your own token.

"""
 https://github.com/D3vd/Meme_Api  -> This API returns a JSON response containing information about random memes from Reddit
 See how this API works: https://meme-api.com/gimme.
"""

"""
Just a note: the bot will respond to you as long as the program is kept running.
If you close your terminal or turn off your computer, it will no longer be running. 
If you want to keep the program running forever, we’ll have to deploy it to another computer in the cloud. However, that is a lesson for another day.
"""

# link to invite the bot to a server (only servers where u r the admin): https://discord.com/oauth2/authorize?client_id=1359857039261569087&permissions=2048&integration_type=0&scope=bot