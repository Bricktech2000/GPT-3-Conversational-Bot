from hashlib import new
from re import S
import discord
import openai
import json
import time

from conversation import Conversation

config = json.load(open("config.json"))

client = discord.Client()

conversations = []

openai.api_key = config['openai_api_key']

start_sequence = "\nBOT:"
restart_sequence = "\n\nPerson:"
session_prompt = open("session_prompt.txt", "r").read()

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence} {question}{start_sequence}'
    prompt_text = prompt_text.replace("BOT", session_prompt.split('\n')[0])
    print(prompt_text)
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
    # print(f'response: str(story)')
    return str(story)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    global session_prompt
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

    response = ask(message.content, session_prompt)

    if response:
        session_prompt = f'{session_prompt}{restart_sequence} {message.content}{start_sequence}{response} '
        await message.channel.send(response)

    # no need for this
    # if not message.content.startswith(config["prefix"]): return

client.run(config["token"])
