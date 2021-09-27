import discord
import matplotlib.colors
import random

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def name(message):

    #changes your name

        newname = message.content[6::]
        user = await message.guild.fetch_member(message.author.id)
        await message.channel.send(user + " changed their name too " + newname)
        await message.author.top_role.edit(name = newname)
    
async def nickname(message):

    #changes your nickname

            newnick = message.content[6::]
            await message.author.edit(nick = newnick)

async def color(message):

    #change color based on hexcode    

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
        
async def randcolor(message):

    #gives you a random color (beware, it changes everyone with the same top rank)

        await message.author.top_role.edit(color = discord.Color.random())
        await message.channel.send("Color changed")

async def randuser(message):

    #says a random user

        memlist = message.guild.members
        selecteduser = memlist[random.randint(0, len(memlist)-1)]
        await message.channel.send(selecteduser.mention)


