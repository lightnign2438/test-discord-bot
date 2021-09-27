import discord
from src import constant



intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

mutelist=[]
modchannelid = constant.modchannelid

async def mute(message):

    #mute's a person by id
        chan = message.guild.get_channel(modchannelid)
        try:
            pa = int(message.content[6::])
        except Exception:              
            await message.channel.send("Invalid input")
            return
        authormessage = message.guild.get_member(message.author.id)
        try:
            muteid = message.guild.get_member(pa)  
        except Exception:              
            await message.channel.send("User does not exist")
            return       
        authorrole = []  
        authorrole = authormessage.roles
        print(authorrole)
        messagerole = []
        messagerole = muteid.roles
        print (messagerole)
        for i in mutelist:
            for j in mutelist:
                if j == i:
                    mutelist.remove(j)

            if authorrole[len(authorrole)-1] >  messagerole[len(messagerole)-1]:
                mutelist.append(pa)
                user = await message.guild.fetch_member(pa)
                user2 = await message.guild.fetch_member(message.author.id)
                await message.chan.send(user.nick + " was just muted by " +  user2.nick)
        else:
            await message.channel.send("you rank is too low")
        print(mutelist)

async def checkmutelist(message):

    #testing command which sends the list of people who are muted
    chan = message.guild.get_channel(modchannelid)
    message.chan.send(mutelist)


async def unmute(message):
#unmute's a person by id



        chan = message.guild.get_channel(modchannelid)
        print(mutelist)
        try:
            id = int(message.content[8::])
        except Exception: 
             
            await message.channel.send("Invalid input")
            return    
        mutelist.remove(id)
        print(mutelist)
        try:
            user = await message.guild.fetch_member(id)
        except Exception:         
            await message.channel.send("User does not exist")
            return    
        user2 = await message.guild.fetch_member(message.author.id)
        await message.chan.send(user.nick + " has been unmuted by " + user2.nick)

async def clearmutelist(message):

    #clear's the list of muted people, (unmutes everyone)

        chan = message.guild.get_channel(modchannelid)
        mutelist.clear()
        user = await message.guild.fetch_member(message.author.id)
        await message.chan.send("mutelist has been cleared by " + user.nick)

