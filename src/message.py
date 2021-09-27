import discord

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def mymes(message):

        #get's number of messages sent by author

        counter=0
        async for i in message.channel.history():
            if message.author==i.author:
                counter+=1
        await message.channel.send("There are " + str(counter) + " messages in this channel by " + str(message.author))