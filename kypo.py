import discord
from discord.ext import commands


admin_helper = (597921286018170900, 292877604053188618, 654822384569942017)

class kypo(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot

    
  

   
    

    
    @commands.command(name="kypo")
    async def main(self, ctx):
        await ctx.send("I am online and active")
        
    @commands.command(name="mail")
    async def mail(self, ctx, *, content):
        if ctx.guild.id == 765695776697352202:
            for i in admin_helper:
                user = self.bot.get_user(i)
                await user.send(f"{ctx.author}({ctx.author.id}) sent a message in {ctx.channel}: {content}")
                
    @commands.Cog.listener()
    async def on_member_join(self, guild, user):
        if guild.id == 765695776697352202:
            kypo_welcome.send(f"Welcome to the Pandora {user.mention}!")
            
    

    
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
    bot.add_cog(kypo(bot))
    kypo_welcome = bot.get_channel(765697240832409650)
