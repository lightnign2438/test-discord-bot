import discord
import os
import random
import matplotlib.colors
import asyncio
import nacl
import ffmpeg

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def song(message):

    #play an song by joining current vc (will only play 1 song for now)
        print("awoijsda")
        print("hiasd")
        VC = message.author.voice.channel
        print(VC)
        connection = await VC.connect(timeout=10) 
        print(connection)
        connection.play(discord.FFmpegPCMAudio(executable="C:/Users/mhutc/OneDrive/Documents/ffmpeg/bin/ffmpeg.exe", source="song.mp3"))
        print("asdhiw")
        while connection.is_playing():
            await asyncio.sleep(0.1)
        await connection.disconect            
        await message.channel.send("disconnected")
        return       