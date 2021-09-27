import discord

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def clonechan(message):

        #clones current channel

        currchan = message.channel
        name = message.content[8::]
        await currchan.clone(name=name)

async def createchan(message):

        #create's channel

        channame = message.content[12::]
        await message.guild.create_text_channel(channame)

async def deltchan(message):

        #delete's channel by name, deosn't work if 2 channels with same name

        channame=message.content[10::]
        for i in message.guild.text_channels:
            if channame==i:
                deltachan=i
                break
        else:
            await message.channel.send("Channel not found, please try again")
        await deltachan.delete()

async def delcurrentchan(message):

        #delete's channel you're in

        await message.channel.delete()
    