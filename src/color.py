import discord
import matplotlib.colors

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)



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