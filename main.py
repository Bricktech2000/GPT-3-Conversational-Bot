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

bot_sequence = "\nBot:"
session_prompt = open("session_prompt.txt", "r").read()
NUM_CHATS = 10
current_chats = []

def ask(question, username_sequence, chat_log=None):
    prompt_text = f'{chat_log}{username_sequence} {question}\n'
    print(prompt_text, end='')
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    print(f'{str(story)}')
    return str(story)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    global current_chats
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


    username = message.author.display_name
    username_sequence = f'\n{username}:'

    current_chats.append(f'{username_sequence} {message.content}')
    print('\n\n\n\n\n', current_chats)
    response = ask(message.content, username_sequence, session_prompt + ''.join(current_chats[-NUM_CHATS:-1]))

    if response and "Bot: " in response:
        # session_prompt += f'{bot_sequence} {response}'
        response = response.replace("Bot: ", "")
        current_chats.append(f'{bot_sequence} {response}')
        await message.channel.send(response)

client.run(config["token"])
