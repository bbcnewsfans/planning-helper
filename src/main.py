import discord
from discord.ext import commands
from discord import app_commands as appcmds


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

token = open('./src/tokens/discord.txt').read()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.display_name}')
    return

@commands.command(name = "sync-app-commands",
                  description = "Syncs application commands.")
@commands.guild_only()
@commands.cooldown(1, 15, commands.BucketType.member)
async def syncAppCommands(ctx:commands.Context):
    if ctx.author.id == 1191850547138007132:
        async with ctx.typing():
            await bot.tree.sync()
        await ctx.reply(content="Commands synced!", mention_author=False)
        return
    else:
        await ctx.reply(content="You don't have the permissions to run this command.", mention_author=False)
        return

@commands.command(name = "sync-db-tables",
                  description = "Syncs databse tables.")
@commands.guild_only()
@commands.cooldown(1, 15, commands.BucketType.member)
async def syncDbTables(ctx:commands.Context):
    if ctx.author.id == 1191850547138007132:
        # create tables
        await ctx.reply(content="Commands synced!", mention_author=False)
        return
    else:
        await ctx.reply(content="You don't have the permissions to run this command.", mention_author=False)
        return

bot.run(token)