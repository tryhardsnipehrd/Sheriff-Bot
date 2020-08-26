import discord
from discord.ext import commands


class cnmc(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command("playerinfo")
    async def playerinfo(self, ctx, player: discord.Member = None):
        if ctx.guild.id == 745985920116850781:
            
            if player == None:
                player = ctx.author
            
            embed=discord.Embed(title="Username",description=f"{player.mention}",color=discord.Color.purple())
            embed.add_field(name="", value=f"**{player.display_name}**", inline = False)
            embed.add_field(name="Country",value="United States of America",inline=False)
            embed.add_field(name="Wins",value="0",inline=False)
            embed.add_field(name="Sent By",value=player, inline=False)
            await ctx.send("This command is in development! Stay tuned!")
            await ctx.send(embed=embed)
        
        
        
def setup(bot):
    bot.add_cog(cnmc(bot))
