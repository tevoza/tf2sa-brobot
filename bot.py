import os
import discord
import pug
from dotenv import load_dotenv

load_dotenv()
TOKEN           = os.getenv('DISCORD_TOKEN')
MAPS            = os.getenv('MAP_LIST').split(",")
SERVER          = os.getenv('SERVER')
RECENT_COOLDOWN = int(os.getenv('RECENT_COOLDOWN'))
PLAYERS_AMOUNT = int(os.getenv('PLAYER_AMOUNT'))

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!start':
        tf2sa_pug = pug.Pug(MAPS, SERVER, RECENT_COOLDOWN, PLAYERS_AMOUNT)
        print(tf2sa_pug)
        await message.channel.send(f'{message.author} started pug')

client.run(TOKEN)
