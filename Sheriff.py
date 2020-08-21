import discord
import typing
import random
import os
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='$')

now = datetime.datetime.now


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print(now)
    
@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)



@bot.command()
async def test(ctx):
    await ctx.trigger_typing()
    await ctx.send("yes")


@bot.command()
async def hello(ctx):
    """Greet yourself!"""
    await ctx.trigger_typing()
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command()
async def cogs(ctx):
    """What cogs are loaded..."""
    await ctx.trigger_typing()
    for i in bot.cogs.keys():
        await ctx.send(i)


@commands.command()
@commands.has_permissions(administrator=True)
async def purge(ctx: commands.Context, limit: int = 100) -> None:
  """ Removes 100 messages in channel.(MOD ONLY) """
  await ctx.channel.purge(limit=int(limit))
    


   
@bot.command()
async def invite(ctx):
    """invite Me!!!"""
    await ctx.send("https://discord.com/oauth2/authorize?client_id=668932488068071427&permissions=8&scope=bot")





bot.run(os.environ["DISCORD_TOKEN"])

