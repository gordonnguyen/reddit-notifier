from discord.ext import tasks
import discord
import time
import asyncio
import asyncpraw
'''
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
'''

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.notify_buildapcsales())
        self.bg_task_2 = self.loop.create_task(self.notify_freebies())
        self.reddit = asyncpraw.Reddit(
            client_id="oK3dTEYR7exUog",
            client_secret="D2sVNa17qetOcmp35iA4LaPwec2Qkg",
            user_agent="MyBot/0.1"
        )

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def notify_buildapcsales(self):
        await self.wait_until_ready()
        channel = self.get_channel(877911044931092491) # channel ID goes here

        while not self.is_closed():
            subreddit = await self.reddit.subreddit("buildapcsales")
            async for submission in subreddit.stream.submissions():
                send_message = submission.title + "\n" + submission.url + "\n"
                await channel.send(send_message)
                await asyncio.sleep(5)

    async def notify_freebies(self):
        await self.wait_until_ready()
        channel = self.get_channel(878108540592603136) # channel ID goes here

        while not self.is_closed():
            subreddit = await self.reddit.subreddit("freebies")
            async for submission in subreddit.stream.submissions():
                send_message = submission.title + "\n" + submission.url + "\n"
                await channel.send(send_message)
                await asyncio.sleep(5)

client = MyClient()
client.run('ODI0Nzk0Mjk2MTE2NzA3MzI4.YF0jjA.qMyUh6TstVUuD2fMPyNPX2VNXv0')