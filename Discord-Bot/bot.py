import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    inspirational_quotes = [
        'I have never seen a thin person drinking  Diet Coke',
        'Many such cases, SAD!',
        'The Industrial Revolution and its consequences have been a disaster for the human race.',
        'It may be the cock that crows, but it is the hen that lays the eggs.',
    ]

    if message.content == 'elephant':
        response = random.choice(inspirational_quotes)
        await message.channel.send(response)

client.run(TOKEN)
