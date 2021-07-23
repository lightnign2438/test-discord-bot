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
    '''if "$announce" in message.content.lower():
        mes = message.content[10::]
        for i in message.guild.channels: FIX '''
    '''if "$role" in message.content.lower():
        para = message.content[6::]
        rolename, perm = para.split()
        if perm.lower() in ("admin","administrator"):
            pe = discord.Permissions(administrator = True)
            await message.guild.create_role(name = rolename, permissions = pe)
        elif perm.isspace() == False:
            pem = perm.lower()
            pe = discord.Permissions(pem = True)
            await message.guild.create_role(name = rolename, permissions = pe)
        elif perm.ispace() == True:
            count = 0
            for i in perm:
                count += count
            if i.isspace() > 53:
               message.channel.send("You have entered too many permissions or have added double spaces, please try again")
            #else:
            #    if i.isspace() < 53:'''
    if "$role" in message.content.lower():
        list2 = ['add_reactions', 'administrator', 'attach_files', 'ban_members', 'change_nickname', 'connect', 'create_instant_invite', 'deafen_members ', 'embed_links', 'external_emojis', 'kick_members', 'manage_channels', 'manage_emojis', 'manage_guild', 'manage_messages', 'manage_nicknames', 'manage_roles', 'manage_webhooks', 'mention_everyone', 'move_members', 'mute_members', 'priority_speaker', 'read_message_history', 'send_messages', 'send_tts_messages', 'speak', 'use_external_emojis', 'use_slash_commands', 'use_voice_activation', 'value', 'view_audit_log', 'view_channel', 'view_guild_insights', 'video']
        para = message.content[6::]
        perms=0
        rolename, perm = para.split()
        rolelist = message.channel.guild.roles
        for i in range(len(rolelist)):
            if rolename == rolelist[i]:
                await message.channel.send("This role already exists")
                break

        if perm.lower() in ("admin","administrator"):
            pe = discord.Permissions(administrator = True)
            await message.guild.create_role(name = rolename, permissions = pe)
        else:
            newrole = await message.guild.create_role(name = rolename)
            list1 = list(para.split(" "))
            decimallist=[] 
            print(list1)
            permdict = {'add_reactions':64, 'administrator':8, 'attach_files':32768, 'ban_members':4, 'change_nickname':67108864, 'connect':1048576, 'create_instant_invite':1, 'deafen_members':8388608, 'embed_links':16384, 'external_emojis':262144, 'kick_members':2, 'manage_channels':16, 'manage_emojis':1073741824, 'manage_guild':32, 'manage_messages':8192, 'manage_nicknames':134217728, 'manage_roles':268435456, 'manage_webhooks':536870912, 'mention_everyone':131072, 'move_members':16777216, 'mute_members':4194304, 'priority_speaker':256, 'read_message_history':65536, 'send_messages':2048, 'send_tts_messages':4096, 'speak':2097152, 'use_external_emojis':262144, 'use_slash_commands':2147483648, 'use_voice_activation':33554432, 'video':512, 'view_audit_log':128, 'view_channel':1024, 'view_guild_insights':524288}
            while len(list1) > 0:
                for j in range(len(list2)):
                    if list1[1] == list2[j]:
                        decimallist.append(permdict[list2[j]])
                        
                        del(list1[1])
            for i in decimallist:
                perms = perms+i

            
            #loop through the hexadecimal values and do a bitwiseor on all of the values, integer values: https://discord.com/developers/applications/835540291016589352/bot convert that to hexadecimal
            print(perms)
            newrole = await newrole.edit(server = 835587187780878337, name = rolename, permissions = perms)
            '''print(list1[1])
            pem = list[1]
            pe = discord.Permissions(pem = True)
            await message.guild.create_role(name = list1[0], permissions = pe)
            '''

                    
testbot.run(os.environ['token'])


'''
errors:
invalid literal for int() with base 16 FIXED
sol:
input isn't str, it's an object.
bug: echo doesn't work FIXED
TODO:
get user id from name&tag
create an annoucements function
create the AOPS function for emojis i.e. :lenny_face: would get a lenny face
plays music from a link
Help feature IMPORTANT
Given a username get an id IMPORTANT
Complete role adder
create a while loop that ends when the list length is 1, then check if the first permission is somewhere in the list2, but first turn all spaces into underscores and lowercase everything, once the permission is found in list2, add that permission into the role.
permissions have an integer object get the integer first from the list2 list then set that to a variable. Next add permissions to that variable then do newrole.edit, and set the permissions to the variable with the integer value of permissions
create a dictionary of the hexadecimal code for each permissions, perform a bitwiseor between the hexadecimal for more than 1 permissions the decimal value of all that is the permssions integer value
'''

