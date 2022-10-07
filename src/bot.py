import argparse
from db import db as db
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import event

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='list') #listar eventos existentes (se tiver um role como argumento mostra apenas eventos desse role)
async def _list(ctx):
    await ctx.send("lista eventos")

@bot.command(name='remind') #criar um evento
async def _remind(ctx, arg_nome, arg_data, arg_hora, arg_tag):
    embed=discord.Embed(title=ctx.user)
    embed.set_author(name=arg_nome)
    embed.add_field(name=f'{arg_hora} - {arg_data}', value=f'@{arg_tag}', inline=False)
    embed.set_footer(text="Lembrete 15 minutos antes")
    await ctx.send(embed=embed)

bot.run(token)