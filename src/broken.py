import discord

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def ban(message):

    #ban command, doesn't work

        banuser = message.content[5::]
        user = str(banuser)
        await discord.Guild.ban('code.test', reason = "somebody banned you", delete_message_days=7)

async def role(message):

    #Broken, integer value wasn't for permissions rather for the bot

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

async def admin(message):

    #Broken, integer value wasn't for permissions rather for the bot

            rolename = message.content[6::]            
            message.guild.create_role(name = rolename)
            print(list1[1])
            pem = list[1]
            pe = discord.Permissions(pem = True)
            await message.guild.create_role(name = list1[0], permissions = adminorstrator)
                  