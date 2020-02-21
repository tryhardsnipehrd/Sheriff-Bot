import discord
import typing
import random
import os
from discord.ext import commands
thing = 12
happy = ["Be you... If someone doesn't like it, tell them to Fuck off...","I believe in you!", "Does anyone even use this?"]

rps1 = ["Rock", "Paper", "Scissors"]

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return

    
    if message.content.startswith('$invite'):
        await message.channel.send('https://discordapp.com/oauth2/authorize?client_id=668932488068071427&scope=bot&permissions=8')
   
    if message.content.startswith('$oops'):
        await message.channel.send('What did you do this time...')

    if 'oof' in message.content:
        await message.channel.send("Big OOF")

    if 'stop' in message.content:
        await message.channel.send("YOU NEED TO STOP IF THEY SAY TO!!!!")

    if message.content.startswith('$optimist'):
        await message.author.send(random.choice(happy))
    
    async def joined(ctx, member: discord.Member):
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

    if 'sheriff' in message.content:
        await message.channel.send("What do you want?? He is busy right now")

    if 'Yuri' in message.content:
        await message.channel.send("DON'T MESS WITH THE SHERIFF'S WAI- I MEAN FRIEND...")
   
    if 'yuri' in message.content:
        await message.channel.send("DON'T MESS WITH THE SHERIFF'S WAI- I MEAN FRIEND...")

    if message.content.startswith('$doki'):
        await message.channel.send("use Y_invite, N_invite, S_invite, M_invite, and MC_invite to add all of the bots to your server!!! (PS... I would not recommend Monika... She is a bitch)")

    if message.content.startswith('$color'):
        await message.channel.send('Here are three numbers for RGB colors...')
        await message.channel.send('3')
        await message.channel.send('2')
        await message.channel.send('1')
        await message.channel.send('Here they are!!!!')
        thing = random.randint(1, 255)
        await message.channel.send(thing)
        thing = random.randint(1, 255)
        await message.channel.send(thing)
        thing = random.randint(1, 255)
        await message.channel.send(thing)
        
    if 'no u' in message.content:
        await message.channel.send("NO YOU!")

    
    await bot.process_commands(message)



@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def greet(ctx, arg):
    """Have me greet the mentioned user!"""
    await ctx.send(f"Hello {arg}!")

@bot.command()
async def hello(ctx):
    """Greet yourself!"""
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command()
async def oops(ctx):
    """When you F*uck something up..."""
    await ctx.send("What did you do wrong this time...")

@bot.command()
async def optimist(ctx):
    """When you are having a bad day..."""
    await ctx.author.send(random.choice(happy))

@bot.command()
async def color(ctx):
    """Get a random color in RGB values!"""
    await ctx.send('Here are three numbers for RGB colors...')
    thing = random.randint(1, 255)
    await ctx.send(thing)
    thing = random.randint(1, 255)
    await ctx.send(thing)
    thing = random.randint(1, 255)
    await ctx.send(thing)
    
@bot.command()
async def rps(ctx, arg):
    """Rock Paper Scissors!"""
    rps2 = random.choice(rps1)
    await ctx.send(f"You chose {arg} and I chose {rps2}")
    if arg == "Scissors":
        if rps2 == "Scissors":
            await ctx.send(f"We seem to have tied, {ctx.author.mention}")

        if rps2 == "Paper":
            await ctx.send(f"Y-You beat me... Congratulations {ctx.author.mention}...")
            
        if rps2 == "Rock":
            await ctx.send(f"And yet another victory for me!")
            

    if arg == "Paper":
        if rps2 == "Paper":
            await ctx.send(f"We seem to have tied, {ctx.author.mention}")

        if rps2 == "Scissors":
            await ctx.send(f"And yet another victory for me!")
            

        if rps2 == "Rock":
            await ctx.send(f"Y-You beat me... Congratulations {ctx.author.mention}")

    if arg == "Rock":
        if rps2 == "Rock":
            await ctx.send(f"We seem to have tied, {ctx.author.mention}")
        
        if rps2 == "Paper":
            
            await ctx.send(f"Another win for me!")
            

        if rps2 == "Scissors":
            await ctx.send(f"Y-You beat me... Congratulations {ctx.author.mention}")

bot.run(os.environ["DISCORD_TOKEN"])

