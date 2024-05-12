import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Enable the privileged members intent

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with keys"))

@client.command()
async def gen(ctx):
    random_string = generate_random_string()
    await ctx.send(f'Here is your key: {random_string}')

def generate_random_string():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = 10
    random_string = ''
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        random_string += characters[random_index]
    return random_string

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
client.run('YOUR_DISCORD_BOT_TOKEN')