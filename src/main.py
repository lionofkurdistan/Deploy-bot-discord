import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = open("TOKEN", "r").read()


@client.event
async def no_content():
  print("content!!")

@client.event
async def no_message(message):
  if message.content.startswith("$neuralbot"):
    await message.channle.send("Hello You said " + message.content[11:])
    
    
    
client.run(TOKEN)
  