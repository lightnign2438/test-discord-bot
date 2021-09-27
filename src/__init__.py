import discord
import os
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

from src import functionality

client.run(os.environ['token'])