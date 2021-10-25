import discord
from embed import embed_maker

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def hello(message):

    #says hello

    await message.channel.send(embed = embed_maker(title = "Hi!", description = "Hello", color = 0x86596b, author = "ta", icon = False, iconi = 'a', url = False, urli = 1))
async def echo(message):

    #echo's what you said
    
    print("test") 
    await message.channel.send(embed = embed_maker(title = "Echo!", description = message.content[6::], color = 0x15c830, author = "ta", icon = False, iconi = 'a', url = False, urli = 1))