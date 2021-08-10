import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$dit'):
        await message.channel.send('Dit me may tg cho!')

@client.event
async def new_message(new):
    await new.channel.send('Fuck You')

client.run('ODI0Nzk0Mjk2MTE2NzA3MzI4.YF0jjA.qMyUh6TstVUuD2fMPyNPX2VNXv0')