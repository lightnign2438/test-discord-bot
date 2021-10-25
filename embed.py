import discord
def embed_maker(title, description, color, author, icon, iconi, url, urli):
    embed = discord.Embed(title = title, description = description, color = color)
    if icon == True:
        embed.set_author(name = author, icon_url = iconi)
    else:
        embed.set_author(name = author)
    if url == True:
        embed.set_thumbnail(url=urli)
    
    
    
    return embed
