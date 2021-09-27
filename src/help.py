import discord

intents = discord.Intents.default()
intents.members = True
testbot = discord.Client(intents = intents)

async def help(message):

    await message.channel.send("hello, prints hi \n echo prints whatever is said after echo \n color, takes in a hexcode and is formatted like this color hexcode, changes the highest rank of the message author and changes it to the hexcode color WARNING: changes everyone elses color with that highest rank \n randcolor changes the highest rank of the message author and gives it a random color, WARNING: changes everyone elses color with that highest rank \n name, changes name format name newname \n nick changes your nickname format: nick newname \n pingroulette, says a random user \n join, bot joins first vc \n clone, clones current channel that you’re in \n deletechannel, deletes current channel you’re in \n deltchan, deletes channel by name, WARNING if 2 channels have the same name, it will delete one of them \n createchan, creates channel format createchan channame \n mymes, says how many messages message author has sent \n dmp creates a dm with someone and gives them an invite, format dmp userid \n mute, mutes a person by id, format mute userid \n unmute, unmutes a person by id format unmute id \n clear mutelist, unmutes everyone \n mutelist test command which sends mutelist or the list of everyone muted \n inorder to use commands just do $ infront of it \n when going into the constants folder please fill in your respective moderation channel id, otherwise various features will not work.")