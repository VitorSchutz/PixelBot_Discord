import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random

client = commands.Bot(command_prefix = ">", case_insenstive = True)

@client.event
async def on_ready():
    print('Entramos como (0.user)'.format(client))

@client.command()
async def Guigay(ctx):
    await ctx.send(f'O Gui foi chamado de gay dnv pelo {ctx.author}')

@client.command()
async def d20(ctx):
    await ctx.send({ctx.author} "Resultado:" {random.randint(1,20))



client.run('ODc4MzEwMTU2NjA4MzcyODA3.YR_UEw.WFMpAreZ1OJjUe_d3puS-S5czsw')