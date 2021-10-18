import discord

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def hello(message):

    #says hello

    await message.channel.send("Hi!")
async def echo(message):

    #echo's what you said
    
    print("test") 
    await message.channel.send(message.content[6::])