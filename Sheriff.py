import discord
import typing
import random
import os
thing = 12



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author.mention}!')
    
    if message.content.startswith('$invite'):
        await message.channel.send('https://discordapp.com/oauth2/authorize?client_id=668932488068071427&scope=bot&permissions=8')

    if message.content.startswith('$help'):
        await message.channel.send('$hello for me to say hello back! Use $optimist to get a DM with some optimism! and use $invite to invite me to server! Also, There are multiple keywords that I respond to... Try to find them all!')
   
    if message.content.startswith('$oops'):
        await message.channel.send('What did you do this time...')

    if 'oops' in message.content:
        await message.channel.send("Should've seen it coming...")

    if 'oof' in message.content:
        await message.channel.send("Big OOF")

    if 'stop' in message.content:
        await message.channel.send("YOU NEED TO STOP IF THEY SAY TO!!!!")

    if message.content.startswith('$optimist'):
        await message.author.send('STAY POSITIVE')
    
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
client.run(os.environ["DISCORD_TOKEN"])

