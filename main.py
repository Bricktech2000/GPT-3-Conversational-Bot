from hashlib import new
import discord
import openai
import json
import time

from conversation import Conversation

config = json.load(open("config.json"))

client = discord.Client()

conversations = []

openai.api_key = config['openai_api_key']

start_sequence = "\nBot:"
restart_sequence = "\n\nPerson:"
session_prompt = open("session_prompt.txt", "r").read()

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

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

    await message.channel.send("GPT-3 anser: ")
    await message.channel.send(ask(message.content, session_prompt))

    # no need for this
    # if not message.content.startswith(config["prefix"]): return

client.run(config["token"])
