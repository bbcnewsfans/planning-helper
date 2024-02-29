import discord
from discord.ext import commands
from discord import app_commands


class VotingCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    # listen for new button presses on polls


def setup(bot:commands.Bot):
    bot.add_cog(VotingCog(bot))