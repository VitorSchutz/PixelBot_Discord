import discord
from discord.ext import comands

client = commands.Bot(command_prexif = ":", case_insenstive = True)

@client.event
async def on_ready():
    print('Entramos como (0.user)'.format(client))

@client.command()
async def Guigay(ctx):
    await ctx.send('O Gui foi chamado de gay dnv pelo {cts.author}')

client.run('ODc4MzEwMTU2NjA4MzcyODA3.YR_UEw.aL_3UKDkK9Op8x9M-MmVY7tkov0')
