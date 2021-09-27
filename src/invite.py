import discord

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def dminv(message):

    #dm's someone an invite to the channel


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

        