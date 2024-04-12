import discord, logging, traceback
from discord.ext import commands
from messageutils import autothread_from_message
import config

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

planninghelperlog = logging.getLogger('discord.planninghelper')

@bot.event
async def on_ready():
    planninghelperlog.info(f'Logged in as {bot.user.name}.')

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(content=f"My ping is {round(bot.latency * 1000)}ms!")

async def publish_to_announcement_channel(message: discord.Message):
    if message.guild.id == config.NewsFansHelper.AnnouncementRelay.from_server_id and message.channel.id == config.NewsFansHelper.AnnouncementRelay.from_channel_id: # log
        send_to = discord.Webhook.from_url(url=config.NewsFansHelper.AnnouncementRelay.to_webhook_url, client=bot)

        files = []
        for attachment in message.attachments:
            await attachment.to_file()

        await send_to.send(content=message.content, files=files)

@bot.event
async def on_message(message: discord.Message):
    await autothread_from_message(message, planninghelperlog)
    await publish_to_announcement_channel(message)
    await bot.process_commands(message)

bot.run(config.NewsFansHelper.token)