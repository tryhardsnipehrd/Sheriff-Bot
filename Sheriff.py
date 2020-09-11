import discord
import typing
import random
import os
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='$', help_command = None)

now = datetime.datetime.now()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print(now)
    bot.load_extension("ddlc")
    bot.load_extension("main")
    bot.load_extension("cnmc")
    
@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)
@bot.command()
async def help(ctx):
    if ctx.guild.id == 645697605829001217:
        embed=discord.Embed(title="Help",description="This is the Help command for the Tryhrd Town Server! It will help you to use me better! ||not in the wrong way||",color=discord.Color.red())
        embed.add_field(name="Programming",value="[ <@597921286018170900> ]",inline=False)
        embed.add_field(name="Development Supporters",value="myself",inline=False)
        embed.add_field(name="Written In",value="Python, Discord.PY",inline=False)
        await ctx.send("This command is in development! Stay tuned!")
        await ctx.send(embed=embed)
    elif ctx.guild.id == 593211246510080000:
        embed=discord.Embed(title="Help",description="This is the Help command for the DDLC Server! It will help you to use me better! ||not in the wrong way||",color=discord.Color.red())
        embed.add_field(name="Programming",value="[ <@597921286018170900> ]",inline=False)
        embed.add_field(name="Development Supporters",value="myself",inline=False)
        embed.add_field(name="Written In",value="Python, Discord.PY",inline=False)
        embed.add_field(name="Misc. Commands",value="hello -- Greet yourself!")
        embed.add_field(name="ㅤ",value="test -- Make sure the bot is working properly!")
        embed.add_field(name="ㅤ",value="rules -- Leave blank to see all the rules, and specify a number to see that specific rule")
        await ctx.send("This command is in development! Stay tuned!")
        await ctx.send(embed=embed)

       


@bot.event
async def on_raw_reaction_add(payload):

    roles = [[748992549619892274, 748992549619892274], [748992549619892274, 748992549619892274],
             [748992549619892274, 748992549619892274], [748992549619892274, 748992549619892274],
             [748923240365424740, 748923240365424740]]

    reactions = [":heart:", ":yellow_heart:", ":green_heart:", ":blue_heart:", ":purple_heart:"]
    message_id = 749054398369497090 #Change this to the id of the actual message
    if payload.message_id == message_id:
        if payload.emoji in reactions:
            user = bot.get_user(payload.user_id)
            for i in range(5):
                if payload.emoji == reactions[i]:
                    await user.add_roles(roles[i][0], roles[i][1])


@bot.command()
async def test(ctx):
    # Store bot message and invoke message in variables:
    await ctx.send("no")
    await ctx.message.delete()

#@bot.command()
#async def hello(ctx):
 #   """Greet yourself!"""
  #  await ctx.trigger_typing()
   # await ctx.send(f'Hello {ctx.author.mention}!')

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
async def yeet(ctx):
    await ctx.send("yeet")
    for i in ctx.guild.members:
        if i.nick != "EAT THE YEET":
            await i.edit(nick="EAT THE YEET")
    
#@bot.event
#async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("Command not found. Please check your spelling and try again!")





bot.run(os.environ["DISCORD_TOKEN"])

