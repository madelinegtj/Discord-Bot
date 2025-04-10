import discord

# MyClient class is created by extending from the discord.Client (see discord API)
# and will be used to interact with Discord API
class MyClient(discord.Client):

  # once Discord bot's login is successful
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # method for bot to read message on the discord channel and respond to them
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello World!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM1OTg1NzAzOTI2MTU2OTA4Nw.GXMShp.zMHFmHQPMQqgPN2QsG6gLe9PUrNtpsuiYiAFx4') # Replace with your own token.