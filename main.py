import os
import discord

from discord.ext import commands
from scrapCl import get_clima_villegas, get_clima_capi, get_clima_la_plata


TOKEN = "MTE3NDQzNzE4NzQzNDA1NzgwOQ.GJcCIT.oqMKckIM3bQmrFD0BJEjTEEsLQxoNjaYwrKTGs"

# Define los intentos del bot
intents = discord.Intents.all()

# Creo una instancia del bot y especifico el comando del prefijo e intentos
bot = commands.Bot(
    command_prefix="!",
    description="Un bot que me tira el clima en el lugar donde estoy y las efemerides del dia",
    intents=intents
)


# El evento corre cuando el bot esta listo
@bot.event
async def on_ready():
    print(f"El bot esta listo. Conectado al {len(bot.guilds)} servidor")


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def get_clima_ville(ctx):
    response = get_clima_villegas()
    await ctx.send(response)


@bot.command()
async def get_clima_caba(ctx):
    response = get_clima_capi()
    await ctx.send(response)


@bot.command()
async def get_clima_lp(ctx):
    response = get_clima_la_plata()
    await ctx.send(response)


bot.run(TOKEN)
