import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random

client = commands.Bot(command_prefix = ">", case_insenstive = True)

@client.event
async def on_ready():
    print('Estamos Online'.format(client))

#Musica
@client.command()
async def join(ctx):
    Ucanal = author.voice.voice_channel
    await ctx.join_voice_channel(Ucanal)


#data
@client.command()
async def Data(ctx):
    await ctx.send(f'Ainda não temos uma data para o RPG {ctx.author}')

# Rolagem de dados
@client.command()
async def d(ctx, numero):
    dado = random.randint(1,int(numero))
    await ctx.send(f'{ctx.author} Resultado: {dado}')



client.run('ODc4MzEwMTU2NjA4MzcyODA3.YR_UEw.Dgi0SYRPuhPa-t8Gpu1PtbtzBf8')