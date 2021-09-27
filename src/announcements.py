import discord

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def announcements(message):

    if message.guild_permissions.author.administrator == True:
        sendmessage = message.content[15::]
        await message.channel.send("@everyone " + sendmessage)
    else:
        message.channel.send("Admin is required to run thisc ommands")