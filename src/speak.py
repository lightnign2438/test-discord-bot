import discord


async def speak(message):
    try:
        VC = message.author.voice.channel
        connection = await VC.connect(timeout=10) 
        connection.play(discord.FFmpegAudio(executable="C:\Users\mhutc\OneDrive\Documents\ffmpeg.exe",source = ""))
        while connection.is_playing():
            asyncio.sleep(0.1)
        connection.disconect
    except Exception:              
        await message.channel.send("disconnected")
        return

#download an mpc and put it in speak file, then put it in sorce