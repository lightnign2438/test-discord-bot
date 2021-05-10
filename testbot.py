import discord
import os
testbot = discord.Client()

@testbot.event
async def on_ready():
    print("Run successful")
@testbot.event
async def on_message(message):
    if message.content.lower() == "$hello":
        await message.channel.send("Hi!")
    if "$echo" in message.content.lower():
        await message.channel.send(message.content[6::])
    if "$color" in message.content.lower():
        desiredcolor = message.content[7::]
        a = int(desiredcolor)
        print(a)
        hexcode = hex(a)
        print(hexcode)
        await message.author.top_role.edit(color = discord.Color(hexcode))
        print(type(message.author.top_role))
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


testbot.run(os.environ['token'])


'''
errors:
invalid literal for int() with base 16
'''

