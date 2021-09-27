import discord
from src import constant

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

modchannelid = constant.modchannelid

async def memberlist(message):

    #test command for memberlist

    chan = message.guild.get_channel(modchannelid)
    message.chan.send(message.guild.members) 

async def channels(message):

    #get's all channel, test command

        for i in message.guild.channels:
            message.chan.send(i)
