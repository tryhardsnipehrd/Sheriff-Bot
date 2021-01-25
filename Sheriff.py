import discord
import typing
import random
import os
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='$')
dokiLockdown = False


statuses = ["Ready to take over | $help","Going to kill SenBot | $help","Waiting to get updated... | $help"]

now = datetime.datetime.now()

kypo_rules = ["Rule 1: No racial slurs. Period.",
             "Rule 2: No spamming. Copy pasta is counted as spamming, and will be dealt with accordingly.",
             "Rule 3: No excessive noise in any of the VC channelsl. EG: Ear rape, Yelling, etc...",
             "Rule 4: Do not spam ping anyone!!! This includes spamming the `$mail` command.",
             "Rule 5: Self Promotion only goes in the dedicated channels. <#765770372523491329> <#765712172901728328>",
             "Rule 6: Do not beg for moderator, admin, or helper. You will get it if you deserve it."]
ddlc_rules = ["Rule 1. Respect other members. | Failure to comply: Warn.",
"Rule 2. Respect the mods. | Failure to comply: Mute.",
"Rule 3. Follow Discord’s TOS at: https://discord.com/terms. | Failure to comply: Ban.",
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
"Rule 20. No ghost pinging. If you ping someone, leave the message. | Failure to comply: Mute + Warn.", 
"Rule 21. No impersonating others with bad intention | Failure to comply: Ban."]


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print(now)
    await bot.change_presence(activity=discord.Game(name=random.choice(statuses)))
    

    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.guild.id == 593211246510080000 and 593217952975683585 not in message.author.roles and dokiLockdown:
        await message.delete()
        

    #if "weed eater" in message.content.lower():
     #   await message.delete()
    #elif "WEÉD EATER" in message.content.upper():
     #   await message.delete()
    if message.channel.id == 633872694609182730 and message.author == 398601531525562369:
        await message.delete()
        
    if bot.user in message.mentions:
        await message.channel.send("WHO DARE MENTION ME")
    
    await bot.process_commands(message)   



@bot.command()
async def test(ctx):
    # Store bot message and invoke message in variables:
    await ctx.send(ctx.author.roles)
    
@bot.command()
async def bday(ctx, mention="no"):
    if mention == "no":
        await ctx.send("Please tell me who to wish a happy birthday to!")
    elif ctx.author.mention == mention:
        await ctx.send("You can't wish yourself a happy birthday!")
    else:
        await ctx.send(f"Happy Happy Birthday, from this bot to you. I hope you have a great day, because I like you! Happy birthday, {mention}")
        
@bot.command(aliases=["rule"])
async def rules(ctx, rule=0):
    if ctx.guild.id == 765695776697352202:
        if rule != 0: await ctx.send(kypo_rules[rule-1])
        else: await ctx.send("\n".join(kypo_rules))
    elif ctx.guild.id == 593211246510080000:
        if rule != 0: await ctx.send(ddlc_rules[rule-1])
        else: await ctx.send("\n".join(ddlc_rules))
          
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user:discord.Member):
    await user.kick()
    await ctx.send(f"{user} has been kicked")
    
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a user to kick. e.g. $kick @user")
    
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user:discord.Member):
    await user.ban()
    await ctx.send(f"{user} has been banned")
    
@ban.error
async def ban_error(ctx, error):
    print("Caught an error on ban")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please provide a user to ban. e.g. $ban @user")
    
    

@bot.command()
async def talk(ctx, *, content):
    kypo_logs = bot.get_channel(765924824731746354)
    await ctx.send(content)
    await ctx.message.delete()
    

@bot.command()
async def cogs(ctx):
    """What cogs are loaded..."""
    await ctx.trigger_typing()
    for i in bot.cogs.keys():
        await ctx.send(i)


@commands.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx: commands.Context, limit: int = 100) -> None:
  """ Removes 100 messages in channel.(MOD ONLY) """
  await ctx.channel.purge(limit=int(limit))
    


   
@bot.command()
async def invite(ctx):
    """invite Me!!!"""
    await ctx.send("https://discord.com/oauth2/authorize?client_id=668932488068071427&permissions=8&scope=bot")
    
@bot.command()
@commands.is_owner()
async def status(ctx, *, status):
    await bot.change_presence(activity=discord.Game(name=status))

@bot.command()
@commands.is_owner()
async def lockdown(ctx):
    if dokiLockdown:
        dokiLockdown = False
        await ctx.send("Lockdown Cancelled!")
    elif not dokiLockdown:
        dokiLockdown = True
        await ctx.send("Lockdown Initiated!")
    
#@bot.event
#async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("Command not found. Please check your spelling and try again!")





bot.run(os.environ["DISCORD_TOKEN"])

