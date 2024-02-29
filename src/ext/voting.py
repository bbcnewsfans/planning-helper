import discord
from discord.ext import commands
from discord import app_commands
from models.Poll import Poll


class VotingCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    # listen for new button presses on polls
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component and interaction.data['custom_id'].startswith('poll-'):
            pollData = interaction.data['custom_id'].split('-')

            try:
                Poll.addVote(pollData[1], pollData[2], interaction.user.id)
            except TypeError:
                await interaction.response.send_message(content="I ran into an error counting your vote.", ephemeral=True)
                return

            await interaction.response.send_message(content="I've counted your vote!", ephemeral=True)
            return
        else:
            return

def setup(bot:commands.Bot):
    bot.add_cog(VotingCog(bot))