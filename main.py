import discord
import openai
import json
import time
import sys
import asyncio
from conversation import Conversation

if len(sys.argv) != 2:
    print("Usage: python main.py <training data file path>")
    exit(1)

config = json.load(open("config.json"))
training_data = open(sys.argv[1], "r").read()
client = discord.Client()
openai.api_key = config['openai_api_key']
conversations = {}

NUM_CHATS = 8 # the number of chats to append to the training data
TEMPERATURE = 0.8 # the "originality" of GPT-3's answers
MAX_TOKENS = 50 # the maximal length of GPt-3's answers
CONVERSATION_TIMEOUT = 60 # seconds. the time to wait before a conversation is considered dead

def GPT_3(chat_log):
    response_object = openai.Completion.create(
        engine="curie",
        prompt=chat_log + '\n',
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"],
    )
    response = str(response_object['choices'][0]['text'])

    print('\n\n\n\n', chat_log)
    print(response)
    return response

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    global conversations

    conversation_id = f'{message.channel.id}%{message.guild.id}'
    current_time = time.time() # seconds
    no_convo = Conversation(0) # This is so the if statemnt below still works
    
    # if CONVERSATION_TIMEOUT seconds have passed since the last message, reset the conversation
    # if no coversation exsists, make one
    if conversations.get(conversation_id, no_convo).timeAlive + CONVERSATION_TIMEOUT < current_time:
        conversations[conversation_id] = Conversation()
    current_convo = conversations[conversation_id]

    username = message.author.display_name
    username_sequence = f'{username}:'
    # https://stackoverflow.com/questions/54304428/get-bots-status-discord-py
    botname = message.guild.get_member(client.user.id).display_name
    botname_sequence = f'{botname}:'
    response = False

    current_convo.Add_Chat(username_sequence, message.content)
    if current_convo.Current_Length() >= 3:
        response = GPT_3(f"{training_data}{''.join(current_convo.chats[-NUM_CHATS:-1])}")
        current_convo.Restart_Timer()

    # if GPT-3 believes it should type next response, send that response
    print(response, botname_sequence)
    if response and botname_sequence in response:
        response = response.replace(f'{botname_sequence} ', '')
        async with message.channel.typing():
            typing_delay = len(response) / 15 # 15 characters per second
            print(f"Typing delay: {typing_delay}s")
            await asyncio.sleep(typing_delay)
        # await message.channel.send(f'CONVERSAITION ID: {conversation_id}\n{response}')
        await message.channel.send(response)

client.run(config["token"])
