from src import discord
import matplotlib.colors
from embed import embed_maker



async def color(message):

    #change color based on hexcode    
       
        
        desiredcolor = message.content[7::]
        embedcolor = "0x" + str(desiredcolor)
        ahex = matplotlib.colors.to_rgb('#'+desiredcolor)
        print(ahex)
        cad = 255*ahex[0]
        cac= 255*ahex[1]
        caa = 255*ahex[2]
        print(cad)
        print(cac)
        print(caa)
        await message.channel.send(embed = embed_maker(title = "Color", description = message.author + " , you set your color to " + str(embedcolor), color = desiredcolor, author = message.author, icon = False, iconi = "a", url = False, urli = 1))
        await message.author.top_role.edit(color = discord.Color.from_rgb(int(cad),int(cac),int(caa)))

        
async def randcolor(message):

    #gives you a random color (beware, it changes everyone with the same top rank)
        c=discord.Color.random()
        await message.channel.send("Color changed")
        await message.channel.send(embed = embed_maker(title = "randomcolor", description = "randcolor " + c, color = c, author = message.author, icon = False, iconi = "a", url = False, urli = 1))
      
        