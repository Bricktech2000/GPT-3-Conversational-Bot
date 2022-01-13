import discord
import json

config = json.load(open("config.json"))

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot: return

    print("hi!")
    await message.channel.send("Hi!")

    # no need for this
    # if not message.content.startswith(config["prefix"]): return

client.run(config["token"])