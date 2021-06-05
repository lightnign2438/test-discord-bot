import discord
import os
import random
import matplotlib.colors
intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)
@testbot.event
async def on_ready():
    print("Run successful")
@testbot.event
async def on_message(message):
    if message.content.lower() == "$hello":
        await message.channel.send("Hi!")
    if "$echo" in message.content.lower():
        await message.channel.send(message.content[6::])
    #fix 
    if "$color" in message.content.lower():
        desiredcolor = message.content[7::]
        ahex = matplotlib.colors.to_rgb('#'+desiredcolor)
        print(ahex)
        cad = 255*ahex[0]
        cac= 255*ahex[1]
        caa = 255*ahex[2]
        print(cad)
        print(cac)
        print(caa)
        await message.author.top_role.edit(color = discord.Color.from_rgb(int(cad),int(cac),int(caa)))
    if "$randcolor" in message.content.lower():
        await message.author.top_role.edit(color = discord.Color.random())
        await message.channel.send("Color changed")
    if "$name" in message.content.lower():
        newname = message.content[6::]
        await message.author.top_role.edit(name = newname)
    if "$perm" in message.content.lower():
        perm = message.content[6::]        
        if perm == "nickname":    
            await message.channel.send(message.author.top_role.permissions.manage_nicknames)
        elif perm in ("roles", "role"):
            await message.channel.send(message.author.top_role.permissions.manage_roles)
        else:
            await message.channel.send("Something went wrong, please try again")
    if "$nick" in message.content.lower():
            newnick = message.content[6::]
            await message.author.edit(nick = newnick)
    if "$memberlist" in message.content.lower():
        print(message.guild.members)  
    if "$pingroulette" in message.content.lower():
        memlist = message.guild.members
        selecteduser = memlist[random.randint(0, len(memlist)-1)]
        await message.channel.send(selecteduser.mention)
    if "$channel" in message.content.lower():
        print(message.guild.channels)
    if "$join" in message.content.lower():
        VC = message.guild.voice_channels[0]
        await message.guild.change_voice_state(channel = VC)
    if "$ban" in message.content.lower():
        banuser = message.content[5::]
        user = int(banuser)
        await discord.Guild.ban('code.test', reason = "somebody banned you", delete_message_days=7)            




testbot.run(os.environ['token'])


'''
errors:
invalid literal for int() with base 16
sol:
input isn't str, it's an object.
'''

