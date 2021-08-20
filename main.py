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
async def d(ctx, numero):
    dado = random.randint(1,int(numero))
    await ctx.send(f'{ctx.author} Resultado: {dado}')



client.run('ODc4MzEwMTU2NjA4MzcyODA3.YR_UEw.Dgi0SYRPuhPa-t8Gpu1PtbtzBf8')