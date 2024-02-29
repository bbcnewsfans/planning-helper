import discord
from discord.ext import commands
from discord import app_commands as appcmds


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

token = open('./src/tokens/discord.txt').read()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.display_name}')
    return

bot.run(token)