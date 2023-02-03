import discord
import requests
import random

# Discord bot setup
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
 print('Bot is ready.')


@client.event
async def on_message(message):
    if message.content.startswith('!meme'):
        # Call the Imgflip API to generate a meme
        response = requests.get('https://api.imgflip.com/get_memes').json()
        memes = response['data']['memes']
        meme = memes[random.randint(1,100)]

        # Send the generated meme to Discord
        await message.channel.send(meme['url'])
client.run('MTA3MTAzMjk1MDA2MzM3ODQ1Mw.GSwQ-p.LkuxqHjaAdD8drX03wpM7wsbLyJpYnC9oFsqps')
# Login to Discord


