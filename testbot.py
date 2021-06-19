import discord
import os
import random
import matplotlib.colors
intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)
@testbot.event
async def on_ready():
    game = discord.Game("Bot is ready")
    await testbot.change_presence(status=discord.Status.online, activity=game)
    
    print("Run successful")
@testbot.event
async def on_message(message):
    print(message.content)
    if message.content.lower() == "$hello":
        await message.channel.send("Hi!")
    if "$echo " in message.content.lower():
        print("test") 
        await message.channel.send(message.content[6::])
    #fix 
    if  "$color" in message.content.lower():
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
    if  "$randcolor" in message.content.lower():
        await message.author.top_role.edit(color = discord.Color.random())
        await message.channel.send("Color changed")
    if  "$name" in message.content.lower():
        newname = message.content[6::]
        await message.author.top_role.edit(name = newname)
    if  "$perm" in message.content.lower():
        perm = message.content[6::]        
        if perm == "nickname":    
            await message.channel.send(message.author.top_role.permissions.manage_nicknames)
        elif perm in ("roles", "role"):
            await message.channel.send(message.author.top_role.permissions.manage_roles)
        else:
            await message.channel.send("Something went wrong, please try again")
    if "$nick"in message.content.lower():
            newnick = message.content[6::]
            await message.author.edit(nick = newnick)
    if "$memberlist" in message.content.lower():
        print(message.guild.members)  
    if "$pingroulette" in message.content.lower():
        memlist = message.guild.members
        selecteduser = memlist[random.randint(0, len(memlist)-1)]
        await message.channel.send(selecteduser.mention)
    if "$channel" in message.content.lower():
        for i in message.guild.channels:
            print(i)
        
    if "$join" in message.content.lower():
        VC = message.guild.voice_channels[0]
        await message.guild.change_voice_state(channel = VC)
    if "$ban" in message.content.lower():
        banuser = message.content[5::]
        user = str(banuser)
        await discord.Guild.ban('code.test', reason = "somebody banned you", delete_message_days=7)            
    if  "$clone" in message.content.lower():
        currchan = message.channel
        name = message.content[8::]
        await currchan.clone(name=name)
    if  message.content.lower() == "$delete channel":
        await message.channel.delete()
    if  "$deltchan" in message.content.lower():
        channame=message.content[10::]
        for i in message.guild.text_channels:
            if channame==i:
                deltachan=i
                break
        else:
            await message.channel.send("Channel not found, please try again")
        await deltachan.delete()
    if "$createtchan" in message.content.lower():
        channame = message.content[12::]
        await message.guild.create_text_channel(channame)
    if "$mymes" in message.content.lower():
        counter=0
        async for i in message.channel.history():
            counter+=1
        await message.channel.send("There are " + str(counter) + " messages in this channel by " + str(message.author))
    if "$mymes" in message.content.lower():
        counter=0
        async for i in message.channel.history():
            if message.author==i.author:
                counter+=1
        await message.channel.send("There are " + str(counter) + " messages in this channel by " + str(message.author))
    if message.content.lower() == "$invite":
        invitee = await message.channel.create_invite(max_age = 120,max_uses = 1, unique =True)
        await message.channel.send(str(invitee))
    if message.content.lower()[0:7] == "$chodm ":
        param = message.content[7::]
        if message.author.dm_channel == None:
            dmchan = await message.author.create_dm()
        else:
            dmchan = message.author.dm_channel
        await dmchan.send(param)
    if message.content.lower() == "$dminv":
        invite = await message.channel.create_invite(max_age = 120, max_uses = 1, unique = True)
        if message.author.dm_channel == None:
            dmchan = await message.author.create_dm()
        else:
            dmchan = message.author.dm_channel
        await dmchan.send(invite)
    if "$dmp" in message.content.lower():
        invite = await message.channel.create_invite(max_age = 120, max_uses = 1, unique = True)
        userid = message.content[5::]
        user = testbot.get_user(int(userid))
        if user == None: 
            await message.send("No users with given ID/name")
        
        if user.dm_channel == None:
            dmchan = await user.create_dm()
        else:
            dmchan = user.dm_channel
        await dmchan.send(invite)
    if message.content.lower() == "$react":
        await message.add_reaction(message.guild.emojis[0])
    
testbot.run(os.environ['token'])


'''
errors:
invalid literal for int() with base 16 FIXED
sol:
input isn't str, it's an object. FIXED
bug: echo doesn't work FIXED
TODO:
get user id from name&tag
create an annoucements function
create the AOPS function for emojis i.e. :lenny_face: would get a lenny face
plays music from a link
'''

