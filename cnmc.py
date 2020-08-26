import discord
from discord.ext import commands


class cnmc(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot
        
        
        
    @commands.command("playerinfo")
    async def playerinfo(self, ctx, player: discord.Member = None):
        if ctx.guild.id == 745985920116850781:
            f=open("player.txt","r+")
            lines=f.readlines()
            lines[0] = "test\n"
            
            
            if player == None:
                player = ctx.author
            
            embed=discord.Embed(title="Player Info!",description=f"This is the player card of {player.display_name}",color=discord.Color.purple())
            embed.add_field(name="Player", value = f"{player.mention}", inline = False)
            embed.add_field(name="Nickname", value=f"**{player.display_name}**", inline = False)
            
            if player.id == 597921286018170900: #Tadbo
                embed.add_field(name="Country",value="United States of America",inline=False)
            
            
            else:
                embed.add_field(name="Country",value="Node 3",inline=False)
                
            if player.id == 597921286018170900: #Tadbo
                embed.add_field(name="Birthday", value="March 28th", inline=False)
                
            else:
                embed.add_field(name="Birthday", value="I... don't rememeber...", inline=False)
            embed.add_field(name="Wins",value="0",inline=False)
            embed.add_field(name="Sent By",value=player, inline=False)
            f.seek(0)
            f.truncate() # make sure we don't leave trailing garbage if the new text is shorter than old one
            f.write(''.join(lines))
            await ctx.send(lines[0])
            await ctx.send(embed=embed)
        
        
        
def setup(bot):
    bot.add_cog(cnmc(bot))
