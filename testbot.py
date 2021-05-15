import discord
import os
import random
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
        '''work in progress, errors ensue'''
        
        desiredcolor = message.content[7::]
        a = int(desiredcolor)
        print(a)
        hexcode = hex(a)
        print(hexcode)
        await message.author.top_role.edit(color = discord.Color(hexcode))
    if "$randcolor" in message.content.lower():
        '''work in progress, errors ensue'''
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



testbot.run(os.environ['token'])


'''
errors:
invalid literal for int() with base 16
sol:
input isn't str, it's an object.
'''

