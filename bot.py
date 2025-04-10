import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM1OTg1NzAzOTI2MTU2OTA4Nw.GXMShp.zMHFmHQPMQqgPN2QsG6gLe9PUrNtpsuiYiAFx4') # Replace with your own token.