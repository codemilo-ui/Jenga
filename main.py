import os
from dotenv import load_dotenv
import discord
import asyncio
import random
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="..",intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=f"on {len(bot.guilds)} servers"))
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Slash commands | watchdog-bot.tk"))
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="Slash commands"))
    print(f"Jenga - Online")
    print(f"Pycord: {discord.__version__}\n")
    print("-------------------------------")


async def ch_pr():
    await bot.wait_until_ready()

    statuses = [f"on {len(bot.guilds)} servers",
                "you"]

    while not bot.is_closed():

        status = random.choice(statuses)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status))

        await asyncio.sleep(10)
bot.loop.create_task(ch_pr())  
bot.run(TOKEN)
