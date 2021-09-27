import discord
import os
import random
import matplotlib.colors
import asyncio
import nacl
import ffmpeg
intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)
mutelist=[]
banlist=[]
@testbot.event
async def on_ready():
    game = discord.Game("Bot is ready")
    await testbot.change_presence(status=discord.Status.online, activity=game)
    
    print("Run successful")
@testbot.event
async def on_message(message):
    for i in range(len(mutelist)):
        print(mutelist[i])
        if mutelist[i]==message.author.id:
            print(message.author.id)
            await message.delete()
    print(message.content)
    
    
    
    if message.content.lower() == "$hello":
        await message.channel.send("Hi!")
    
    #echo's what you said

    if "$echo " in message.content.lower():
        print("test") 
        await message.channel.send(message.content[6::])

    #change color based on hexcode    

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

    #gives you a random color (beware, it changes everyone with the same top rank)

    if  "$randcolor" in message.content.lower():
        await message.author.top_role.edit(color = discord.Color.random())
        await message.channel.send("Color changed")

    #changes your name

    if  "$name" in message.content.lower():
        newname = message.content[6::]
        user = await message.guild.fetch_member(message.author.id)
        await message.channel.send(user + " changed their name too " + newname)
        await message.author.top_role.edit(name = newname)

    #changes your nickname

    if "$nick"in message.content.lower():
            newnick = message.content[6::]
            await message.author.edit(nick = newnick)

    #test command for memberlist

    if "$memberlist" in message.content.lower():
        print(message.guild.members)  
    
    #says a random user

    if "$pingroulette" in message.content.lower():
        memlist = message.guild.members
        selecteduser = memlist[random.randint(0, len(memlist)-1)]
        await message.channel.send(selecteduser.mention)

    #get's all channel, test command

    if "$channel" in message.content.lower():
        for i in message.guild.channels:
            print(i)


    #ban command, doesn't work

    if "$ban" in message.content.lower():
        banuser = message.content[5::]
        user = str(banuser)
        await discord.Guild.ban('code.test', reason = "somebody banned you", delete_message_days=7)            

    #clones current channel

    if  "$clone" in message.content.lower():
        currchan = message.channel
        name = message.content[8::]
        await currchan.clone(name=name)

    #delete's channel you're in

    if  message.content.lower() == "$deletechannel":
        await message.channel.delete()

    #delete's channel by name, deosn't work if 2 channels with same name

    if  "$deltchan" in message.content.lower():
        channame=message.content[10::]
        for i in message.guild.text_channels:
            if channame==i:
                deltachan=i
                break
        else:
            await message.channel.send("Channel not found, please try again")
        await deltachan.delete()

    #create's channel

    if "$createtchan" in message.content.lower():
        channame = message.content[12::]
        await message.guild.create_text_channel(channame)

    #get's number of messages sent by author

    if "$mymes" in message.content.lower():
        counter=0
        async for i in message.channel.history():
            if message.author==i.author:
                counter+=1
        await message.channel.send("There are " + str(counter) + " messages in this channel by " + str(message.author))

    #dm's someone an invite to the channel

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
    
    #mute's a person by id

    if "$mute" in message.content.lower():
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
                await message.channel.send(user.nick + " was just muted by " +  user2.nick)
        else:
            await message.channel.send("you rank is too low")
        print(mutelist)



        

    #unmute's a person by id





    if "$unmute" in message.content.lower():
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
        await message.channel.send(user.nick + " has been unmuted by " + user2.nick)

    #clear's the list of muted people, (unmutes everyone)

    if "$clear mutelist" in message.content.lower():
        mutelist.clear()
        user = await message.guild.fetch_member(message.author.id)
        await message.channel.send("mutelist has been cleared by " + user.nick)

    #testing command which sends the list of people who are muted

    if "$mutelist" in message.content.lower():
        message.channel.send(mutelist)

    if "$help" in message.content.lower():
        await message.channel.send("hello, prints hi \n echo prints whatever is said after echo \n color, takes in a hexcode and is formatted like this color hexcode, changes the highest rank of the message author and changes it to the hexcode color WARNING: changes everyone elses color with that highest rank \n randcolor changes the highest rank of the message author and gives it a random color, WARNING: changes everyone elses color with that highest rank \n name, changes name format name newname \n nick changes your nickname format: nick newname \n pingroulette, says a random user \n join, bot joins first vc \n clone, clones current channel that you’re in \n deletechannel, deletes current channel you’re in \n deltchan, deletes channel by name, WARNING if 2 channels have the same name, it will delete one of them \n createchan, creates channel format createchan channame \n mymes, says how many messages message author has sent \n dmp creates a dm with someone and gives them an invite, format dmp userid \n mute, mutes a person by id, format mute userid \n unmute, unmutes a person by id format unmute id \n clear mutelist, unmutes everyone \n mutelist test command which sends mutelist or the list of everyone muted \n inorder to use commands just do $ infront of it")

        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Broken, integer value wasn't for permissions rather for the bot

    if "$role" in message.content.lower():
        list2 = ['add_reactions', 'administrator', 'attach_files', 'ban_members', 'change_nickname', 'connect', 'create_instant_invite', 'deafen_members ', 'embed_links', 'external_emojis', 'kick_members', 'manage_channels', 'manage_emojis', 'manage_guild', 'manage_messages', 'manage_nicknames', 'manage_roles', 'manage_webhooks', 'mention_everyone', 'move_members', 'mute_members', 'priority_speaker', 'read_message_history', 'send_messages', 'send_tts_messages', 'speak', 'use_external_emojis', 'use_slash_commands', 'use_voice_activation', 'view_audit_log', 'view_channel', 'view_guild_insights', 'video']
        para = message.content[6::]
        perms=0
        perm = []
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
            while len(list1)>1:
                for j in list2:
                    print("list1 len:" + str(len(list1)))
                    if len(list1)>1:
                        if list1[1] == j:
                            decimallist.append(permdict[j])
                            del(list1[1])
                    else:
                        print("break")
                        break
                
                
            '''while len(list1) > 0:
                for j in range(len(list2)):
                    if list1[1] == list2[j]:
                        decimallist.append(permdict[list2[j]])
                        
                        del(list1[1])'''
            for i in decimallist:
                perms = perms+i

            
            #loop through the hexadecimal values and do a bitwiseor on all of the values, integer values: https://discord.com/developers/applications/835540291016589352/bot convert that to hexadecimal
            print(perms)
            newrole = await newrole.edit(server = 835587187780878337, name = rolename, permissions = 2097152)
            
        if "$admin" in message.content.lower():

            rolename = message.content[6::]            
            message.guild.create_role(name = rolename)
            print(list1[1])
            pem = list[1]
            pe = discord.Permissions(pem = True)
            await message.guild.create_role(name = list1[0], permissions = adminorstrator)
            
    #play an song by joining current vc (will only play 1 song for now)
    if message.content.lower() ==  "$song":
        print("awoijsda")
        print("hiasd")
        VC = message.author.voice.channel
        print(VC)
        connection = await VC.connect(timeout=10) 
        print(connection)
        connection.play(discord.FFmpegPCMAudio(executable="C:/Users/mhutc/OneDrive/Documents/ffmpeg/bin/ffmpeg.exe", source="song.mp3"))
        print("asdhiw")
        while connection.is_playing():
            await asyncio.sleep(0.1)
        await connection.disconect            
        await message.channel.send("disconnected")
        return       



async def speak(message):
    print("play worked")
    try:
        VC = message.author.voice.channel
        connection = await VC.connect(timeout=10) 
        connection.play(discord.FFmpegAudio(executable="C:/Users/mhutc/OneDrive/Documents/test discord bot/botenvtest/Lib/site-packages/ffmpeg/_ffmpeg.py", source = "src/song.mp3"))
        while connection.is_playing():
            asyncio.sleep(0.1)
        connection.disconect
    except Exception:              
        await message.channel.send("disconnected")
        return                    
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


Final Project!: 
let a user store video links of songs on a text based json file, then when they type !songroulette, it picks a random song, joins the current users vc, and plays the song

'''

