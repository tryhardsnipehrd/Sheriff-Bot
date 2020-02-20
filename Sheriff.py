import discord
import typing
import random
import os
from discord.ext import commands
thing = 12
happy = ["Be you... If someone doesn't like it, tell them to Fuck off...","I believe in you!", "Does anyone even use this?"]

rps = ["Rock", "Paper", "Scissors"]

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return

    
    if message.content.startswith('s.invite'):
        await message.channel.send('https://discordapp.com/oauth2/authorize?client_id=668932488068071427&scope=bot&permissions=8')
   
    if message.content.startswith('s.oops'):
        await message.channel.send('What did you do this time...')

    if 'oof' in message.content:
        await message.channel.send("Big OOF")

    if 'stop' in message.content:
        await message.channel.send("YOU NEED TO STOP IF THEY SAY TO!!!!")

    if message.content.startswith('s.optimist'):
        await message.author.send(random.choice(happy))
    
    async def joined(ctx, member: discord.Member):
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

    if 'sheriff' in message.content:
        await message.channel.send("What do you want?? He is busy right now")

    if 'Yuri' in message.content:
        await message.channel.send("DON'T MESS WITH THE SHERIFF'S WAI- I MEAN FRIEND...")
   
    if 'yuri' in message.content:
        await message.channel.send("DON'T MESS WITH THE SHERIFF'S WAI- I MEAN FRIEND...")

    if message.content.startswith('s.doki'):
        await message.channel.send("use Y_invite, N_invite, S_invite, M_invite, and MC_invite to add all of the bots to your server!!! (PS... I would not recommend Monika... She is a bitch)")

    if message.content.startswith('s.color'):
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
#Rock Paper Scissors of HELL
    if message.content.startswith("s.rps"):
        if "Scissors" in message.content:
            rps2 = random.choice(rps)
            await message.channel.send(f"I chose {rps2} and you chose scissors!")
            if rps2 == "Scissors":
                await message.channel.send("DRAW")
            elif rps2 == "Paper":
                await message.channel.send("I can't believe you beat me...")
            elif rps2 == "Rock":
                await message.channel.send("I WIN!!!")
            else:
                await message.channel.send("How did you get this?")
        elif "Paper" in message.content:
            rps2 = random.choice(rps)
            await message.channel.send(f"I chose {rps2} and you chose Paper!")
            if rps2 == "Paper":
                await message.channel.send("DRAW")
            elif rps2 == "Rock":
                await message.channel.send("I can't believe you beat me...")
            elif rps2 == "Scissors":
                await message.channel.send("I WIN!!!")
        elif "Rock" in message.content:
            rps2 = random.choice(rps)
            await message.channel.send(f"I chose {rps2} and you chose Rock!")
            if rps2 == "Rock":
                await message.channel.send("DRAW")
            elif rps2 == "Scissors":
                await message.channel.send("I can't believe you beat me...")
            elif rps2 == "Paper":
                await message.channel.send("I WIN!!!")
        else:
            await message.channel.send("Please use a valid Rock Paper or Scissor...")
    
    await bot.process_commands(message)



@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def greet(ctx, arg):
    await ctx.send(f"hello {arg}")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command()
async def oops(ctx):
    await ctx.send("What did you do wrong this time...")

@bot.command()
async def color(ctx):
        await ctx.send('Here are three numbers for RGB colors...')
        thing = random.randint(1, 255)
        await ctx.send(thing)
        thing = random.randint(1, 255)
        await ctx.send(thing)
        thing = random.randint(1, 255)
        await ctx.send(thing)
bot.run(os.environ["DISCORD_TOKEN"])

