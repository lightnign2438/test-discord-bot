import discord
import os
import random
import matplotlib.colors
import asyncio
import nacl
import ffmpeg
from src import constant

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)
musicid = constant.musicid
async def song(message):

    #play an song by joining current vc (will only play 1 song for now)
        chann = testbot.get_channel(musicid)
        print("awoijsda")
        print("hiasd")
        VC = message.author.voice.channel
        print(VC)
        connection = await VC.connect(timeout=10) 
        print(connection)
        connection.play(discord.FFmpegPCMAudio(executable="C:/Users/mhutc/OneDrive/Documents/ffmpeg/bin/ffmpeg.exe", source="song.mp3"))
        print("asdhiw")
        embed = discord.Embed(title = "Song", description = "this is a song", colour=0x763B83)
        embed.set_author(name = "ta", icon_url = "https://tse2.mm.bing.net/th?id=OIP.MWIKFuQ74sQEZUUCFijgwgHaJm&pid=Api&P=0&w=300&h=300")
        embed.set_thumbnail(url="https://tse2.mm.bing.net/th?id=OIP.MWIKFuQ74sQEZUUCFijgwgHaJm&pid=Api&P=0&w=300&h=300")
        await message.channel.send(embed = embed)
        while connection.is_playing():
            await asyncio.sleep(0.1)
        await connection.disconect            
        await message.chann.send("disconnected")
        return       