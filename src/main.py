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

@bot.command()
async def publish(ctx: commands.Context):
    if bot.get_guild(config.NewsFansHelper.server_id).get_role(config.NewsFansHelper.board_role_id):
        if ctx.channel.type in [discord.ChannelType.news_thread, discord.ChannelType.public_thread, discord.ChannelType.private_thread] and ctx.channel.parent.id == config.NewsFansHelper.AnnouncementRelay.from_channel_id:
            send_to = discord.Webhook.from_url(url=config.NewsFansHelper.AnnouncementRelay.to_webhook_url, client=bot)

            msg = ctx.channel.starter_message

            ping = f"\n\n<@&{config.NewsFansHelper.AnnouncementRelay.ping_role_id}>"
            as_author = False

            if msg:
                content = msg.content

                if f"<@&{config.NewsFansHelper.AnnouncementRelay.FlagRoleIds.noping}>" in content:
                    content = content.replace(f"<@&{config.NewsFansHelper.AnnouncementRelay.FlagRoleIds.noping}>", "")
                    ping = ""
                
                if f"<@&{config.NewsFansHelper.AnnouncementRelay.FlagRoleIds.asme}>" in content:
                    content = content.replace(f"<@&{config.NewsFansHelper.AnnouncementRelay.FlagRoleIds.asme}>", "")
                    as_author = True
                
                files = []

                for attachment in msg.attachments:
                    a = await attachment.to_file()
                    files.append(a)
                
                if as_author:
                    await send_to.send(content=(content + ping), files=files, username=msg.author.global_name, avatar_url=msg.author.display_avatar.url)
                else:
                    await send_to.send(content=(content + ping), files=files)
                
                await ctx.send(content="Published!")
            else:
                await ctx.send(content="Message not found!")
                return
        else:
            await ctx.send(content="This is not a thread linked to an announcement!")
            return
    else:
        await ctx.send(content="You don't have the permissions to run this command.")
        return

@bot.event
async def on_message(message: discord.Message):
    text_types = [discord.ChannelType.text, discord.ChannelType.news]
    if message.channel.type in text_types:
        await autothread_from_message(message, planninghelperlog)
    await bot.process_commands(message)

bot.run(config.NewsFansHelper.token)