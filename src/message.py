import discord
from embed import embed_maker
intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def mymes(message):

        #get's number of messages sent by author

        counter=0
        async for i in message.channel.history():
            if message.author==i.author:
                counter+=1

        await message.channel.send(embed = embed_maker(title = "Nummessages", description = "There are " + str(counter) + " messages in this channel by " + message.author, color = 0x7a805d, author = message.author, icon = False, iconi = "a", url = False, urli = 1))
        