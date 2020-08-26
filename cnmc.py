import discord
from discord.ext import commands


class cnmc(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command("thingy")
    async def thingy(self, ctx):
        await ctx.send("I am online and working")
        
        
        
def setup(bot):
    bot.add_cog(cnmc(bot))
