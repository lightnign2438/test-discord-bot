import discord
from embed import embed_maker
intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def announcements(message):

    if message.author.guild_permissions.administrator == True:
        sendmessage = message.content[15::]
        await message.channel.send(embed = embed_maker(title = "Announcement", description = "@everyone " + sendmessage, color = 0x86596b, author = message.author, icon = False, iconi = "a", url = False, urli = 1))
    else:
        message.channel.send("Admin is required to run this commands")