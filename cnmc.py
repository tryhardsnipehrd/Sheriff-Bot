import discord
from discord.ext import commands


class cnmc(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command("thingy")
    async def playerinfo(self, ctx, player = None):
        if ctx.guild.id == 745985920116850781:
            if player = None:
                player = ctx.author
            else: 
                player = player.strip("<>@!")
            embed=discord.Embed(title="Username",description="[ <@597921286018170900> ]",color=discord.Color.purple())
            embed.add_field(name="Country",value="United States of America",inline=False)
            embed.add_field(name="Wins",value="0",inline=False)
            embed.add_field(name="Sent By",value=player, inline=False)
            await ctx.send("This command is in development! Stay tuned!")
            await ctx.send(embed=embed)
        
        
        
def setup(bot):
    bot.add_cog(cnmc(bot))
