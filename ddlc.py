import discord
from discord.ext import commands

rules = ["Rule 1. Respect other members. | Failure to comply: Warn.",
"Rule 2. Respect the mods. | Failure to comply: Mute.",
"Rule 3. Follow Discord’s TOS at: https://discord.com/terms. | Failure to comply: Warn.",
"Rule 4. Don't discriminate against LGBTQIA+ | Failure to comply: Ban.",
"Rule 5. Respect other people's opinions | Failure to comply: Mute.",
"Rule 6. Swearing is ok, but don't go overboard. ex: N||ice ca||r, F|| no  ||t, C||hon||k etc. | Failure to comply: Ban",
"Rule 7. No DM advertising. | Failure to comply: Warn.",
"Rule 8. Racism will not be tolerated. | Failure to comply: Ban.",
"Rule 9. Don't start fights/arguments. | Failure to comply: Mute.",
"Rule 10. NSFW Content will not be tolerated anywhere in this server and it never will. | Failure to comply: Ban.",
"Rule 11. Don't spam because it serves no purpose except to annoy people, as you will not gain experience from spamming. Copy pasta is counted as spam. | Failure to comply: Mute.",
"Rule 12. We don't have any 18+ channels so don't lie about your age. | Failure to comply: Warn.",
"Rule 13. No jokes about terrorist attacks and/or famous deaths. | Failure to comply: Warn.",
"Rule 14. Please use channels for their purpose to avoid mass hysteria. | Failure to comply: Warn.",
"Rule 15. No furry except OwO and UwU as it breaks rule 10. | Failure to comply: Ban",
"Rule 16. Pictures of Sayori hanging will not be tolerated. | Failure to comply: Warning",
"Rule 17. Don't raid ex: Spam, Mass ping, etc. | Failure to comply: Ban.",
"Rule 18. Don’t steal fan art. If you didn’t draw it, don’t claim it as your own. | Failure to comply: Warn + Mute.",
"Rule 19. You must be at least 13 years old (as per Discord’s TOS Rule 3). | Failure to comply: Ban.",
"Rule 21. No ghost pinging. If you ping someone, leave the message. | Failure to comply: Mute + Warn.", 
"Rule 22. No impersonating others with bad intention | Failure to comply: Ban."]


"""A simple cog example with simple commands. Showcased here are some check decorators, and the use of events in cogs.
For a list of inbuilt checks:
http://dischttp://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checksordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checks
You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689
For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""


class ddlc(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot

    
  

    @commands.command(name='admin')
    @commands.has_role("Owner")
    async def only_me(self, ctx):
        """A simple command which only responds to the owner of the bot."""

        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!!')
        
    @commands.command(name="ddlc")
    async def ddlc(self, ctx):
        if ctx.guild.id == 593211246510080000:
            await ctx.send("is currently loaded and working")
        else:
            await ctx.send("is not available in this server")
    
    @commands.command(name="rules", aliases=["rule"])
    async def delete(self, ctx, rule=0):
        if rule != 0: await ctx.send(rules[rule-1])
        else: await ctx.send("\n".join(rules))
        
    

    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Event Listener which is called when a user is banned from the guild.
        For this example I will keep things simple and just print some info.
        Notice how because we are in a cog class we do not need to use @bot.event
        For more information:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban
        Check above for a list of events.
        """
        if self.guild.id == 593211246510080000:
            guild.get_channel(596612034091679764).send(f'sadly, {user.name}-{user.id} was banned from {guild.name}-{guild.id} for unknown reasons...')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(ddlc(bot))

