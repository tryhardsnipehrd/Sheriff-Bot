import discord
import typing
import random
import os
from discord.ext import commands
import datetime

# Cog imports


bot = commands.Bot(command_prefix='$')



statuses = ["Ready to take over | $help","Watching over | $help","Waiting to get updated... | $help"]

now = datetime.datetime.now()




@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print(now)
    await bot.change_presence(activity=discord.Game(name=random.choice(statuses)))

    # Loading all the cogs?
    await bot.add_cog(main(bot))
    

    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

        



    
 
        
    if bot.user in message.mentions:
        await message.channel.send("WHO DARE MENTION ME")
    
    await bot.process_commands(message)   



@bot.command()
async def test(ctx):
    await ctx.send("testing")
    

    
@bot.command()
async def bday(ctx, mention=None):
    if mention == None:
        await ctx.send("Please tell me who to wish a happy birthday to!")
    elif ctx.author.mention == mention:
        await ctx.send("You can't wish yourself a happy birthday!")
    else:
        await ctx.send(f"Happy Happy Birthday, from this bot to you. I hope you have a great day, because I like you!\nHappy birthday, {mention}")
        

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
    message = ctx
    await ctx.message.delete()
    await message.send(content)
    

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



    
    
@bot.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandNotFound):
         await ctx.send("Command not found. Please check your spelling and try again!")





bot.run(os.environ["DISCORD_TOKEN"])

