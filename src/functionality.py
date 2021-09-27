from src import basic,broken,channel,color,constant,help,invite,message,mute,speak,test,userfunction
from src import client
import discord
import os
import random
import matplotlib.colors
import asyncio
import nacl
import ffmpeg

@client.event
async def on_ready():
    game = discord.Game("Bot is ready")
    await client.change_presence(status=discord.Status.online, activity=game)
    
    print("Run successful")
@client.event
async def on_message(message):
    for i in range(len(mute.mutelist)):
        print(mute.mutelist[i])
        if mute.mutelist[i]==message.author.id:
            print(message.author.id)
            await message.delete()
    print(message.content)
    if message.content.lower() == "$hello":
            await basic.hello(message)
    
    #echo's what you said

    if "$echo " in message.content.lower():
        await basic.echo(message)

    #change color based on hexcode    

    if  "$color" in message.content.lower():
        await userfunction.color(message)

    #gives you a random color (beware, it changes everyone with the same top rank)

    if  "$randcolor" in message.content.lower():
        await userfunction.randcolor(message)

    #changes your name

    if  "$name" in message.content.lower():
        await userfunction.name(message)

    #changes your nickname

    if "$nick"in message.content.lower():
            await userfunction.nickname(message)

    #test command for memberlist

    if "$memberlist" in message.content.lower():
        await test.memberlist(message)
    
    #says a random user

    if "$pingroulette" in message.content.lower():
        await userfunction.randuser(message)

    #get's all channel, test command

    if "$channel" in message.content.lower():
        await test.channels(message)

         

    #clones current channel

    if  "$clone" in message.content.lower():
        await channel.clonechan(message)

    #delete's channel you're in

    if  message.content.lower() == "$deletechannel":
        await channel.deltcurrentchan(message)

    #delete's channel by name, deosn't work if 2 channels with same name

    if  "$deltchan" in message.content.lower():
        await channel.deltchan(message)

    #create's channel

    if "$createtchan" in message.content.lower():
        await channel.createchan(message)

    #get's number of messages sent by author

    if "$mymes" in message.content.lower():
        await message.mymes(message)

    #dm's someone an invite to the channel

    if "$dmp" in message.content.lower():
        await invite.dminv(message)

    '''if message.content.lower() == "$react":
        await message.add_reaction(message.guild.emojis[0])'''
    
    #mute's a person by id

    if "$mute" in message.content.lower():
        await mute.mute(message)



        

    #unmute's a person by id





    if "$unmute" in message.content.lower():
        await mute.unmute(message)

    #testing command which sends the list of people who are muted

    if "$mutelist" in message.content.lower():
        await mute.checkmutelist(message)





    if "$help" in message.content.lower():
        await help.help(message)

        
            
    
    
            
    #play an song by joining current vc (will only play 1 song for now)
    if message.content.lower() ==  "$song":
        await speak.song(message) 
    if "$announcements" in message.content.lower():
        if message.guild_permissions.author.administrator == True:
            sendmessage = message.content[15::]
            await message.channel.send("@everyone " + sendmessage)
        else:
            message.channel.send("Admin is required to run thisc ommands")

        
                  


