import discord
from embed import embed_maker


async def clonechan(message):

        #clones current channel

        currchan = message.channel
        name = message.content[8::]
        await currchan.clone(name=name)
        await message.channel.send(embed = embed_maker(title = "Clonedchannel", description = message.author + " cloned " + currchan, color = 0x7a805d, author = message.author, icon = False, iconi = "a", url = False, urli = 1))
        

async def createchan(message):

        #create's channel

        channame = message.content[12::]
        await message.guild.create_text_channel(channame)
        await message.channel.send(embed = embed_maker(title = "Clonedchannel", description = message.author + " created a channel called " + channame, color = 0x7a805d, author = message.author, icon = False, iconi = "a", url = False, urli = 1))

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
    