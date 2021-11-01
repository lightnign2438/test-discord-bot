import discord
import matplotlib.colors
import random
from embed import embed_maker

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def name(message):

    #changes your rolename

        newname = message.content[6::]
        user = await message.guild.fetch_member(message.author.id)
        await message.channel.send(str(user) + " changed their name too " + str(newname))
        await message.author.top_role.edit(name = newname)
        await message.channel.send(embed = embed_maker(title = "Rolename", description = str(user) + " changed their name too " + str(newname), color = 0x7a805d, author = message.author, icon = False, iconi = "a", url = False, urli = 1))
    
async def nickname(message):

    #changes your nickname

            newnick = message.content[6::]
            await message.author.edit(nick = newnick)

            await message.channel.send(embed = embed_maker(title = "Nick", description = str(message.author)+" set their nick/name to " + str(newnick), color = 0x7a805d, author = message.author, icon = False, iconi = "a", url = False, urli = 1))

async def color(message):

    #change color based on hexcode    
        desiredcolor = message.content[7::]
        embedcolor = "#" + (desiredcolor)
        ahex = matplotlib.colors.to_rgb('#'+desiredcolor)
        print(ahex)
        cad = 255*ahex[0]
        cac= 255*ahex[1]
        caa = 255*ahex[2]
        print(cad)
        print(cac)
        print(caa)
        await message.channel.send(embed = embed_maker(title = "Color", description = str(message.author) + " , you set your color to " + str(embedcolor), color = int(desiredcolor,16), author = message.author, icon = False, iconi = "a", url = False, urli = 1))
        await message.author.top_role.edit(color = discord.Color.from_rgb(int(cad),int(cac),int(caa)))
        
async def randcolor(message):

    #gives you a random color (beware, it changes everyone with the same top rank)
        c=discord.Color.random()
        print(c)
        await message.author.top_role.edit(color = c)
        await message.channel.send(embed = embed_maker(title = "randomcolor", description = "Randcolor " + str(c), color = c, author = message.author, icon = False, iconi = "a", url = False, urli = 1))

async def randuser(message):

    #says a random user

        memlist = message.guild.members
        selecteduser = memlist[random.randint(0, len(memlist)-1)]

        await message.channel.send(embed = embed_maker(title = "Randuser", description = selecteduser.mention+ " was picked.", color = 0x7a805d, author = selecteduser, icon = False, iconi = "a", url = False, urli = 1))


