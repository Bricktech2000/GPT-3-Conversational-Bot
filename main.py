from hashlib import new
import discord
import json
import time

from conversation import Conversation

config = json.load(open("config.json"))

client = discord.Client()

conversations = []

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot: return

    convo = None

    for i in conversations:
        if time.time() - i.timeAlive > 5000:
            conversations.pop(i)
            continue

        if message.channel == i.channel:
            convo = i
    
    if convo == None:
        convo = Conversation(message.author, message.channel, None)

    print("hi!")
    await message.channel.send("Hi!")

    # no need for this
    # if not message.content.startswith(config["prefix"]): return

client.run(config["token"])