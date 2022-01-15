import discord
import openai
import json
import time
import sys
import asyncio
from conversation import Conversation
from cypher import Change_Usernames, genHashUsername

if len(sys.argv) != 3:
    print("Usage: python main.py <decision training data file path> <response training data file path>")
    exit(1)

config = json.load(open("config.json"))
decision_training_data = open(sys.argv[1], "r").read()
response_training_data = open(sys.argv[2], "r").read()
client = discord.Client()
openai.api_key = config['openai_api_key']
conversations = {}

NUM_CHATS = 8 # the number of chats to append to the training data
TEMPERATURE = 0.8 # the "originality" of GPT-3's answers
MAX_TOKENS = 50 # the maximal length of GPt-3's answers
CONVERSATION_TIMEOUT = 60 # seconds. the time to wait before a conversation is considered dead
TIME_DELAY = 0 # seconds. The time to wait between sending new messages to API

<<<<<<< HEAD
def GPT_3(chat_log):
    chat_log = Change_Usernames(chat_log)
=======
def GPT_3(engine, chat_log, max_tokens=MAX_TOKENS):
>>>>>>> 47d15e328ea59d5087c615a703bbeeacc28aec4a
    response_object = openai.Completion.create(
        engine=engine,
        prompt=chat_log,
        temperature=TEMPERATURE,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"],
    )
    response = str(response_object['choices'][0]['text'])

    # print('\n\n\n\n', chat_log)
    # print(response)
    return response

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    global conversations

    conversation_id = f'{message.channel.id}%{message.guild.id}'

    # if CONVERSATION_TIMEOUT seconds have passed since the last message, reset the conversation
    # if no coversation exsists, make one
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation(CONVERSATION_TIMEOUT, TIME_DELAY)
    current_convo = conversations[conversation_id]

    username = message.author.display_name
    botname = message.guild.get_member(client.user.id).display_name
<<<<<<< HEAD
    botname = genHashUsername(botname)
    botname_sequence = f'{botname}:'
    response = False
=======
    response = None

    print(f'received message: {message.content}')
>>>>>>> 47d15e328ea59d5087c615a703bbeeacc28aec4a

    # add the message to the conversation and generate the "Should respond?" message
    should_fetch = current_convo.should_fetch()
    current_convo.add_chat(username, message.content)
    if should_fetch:
        response = GPT_3('curie', decision_training_data + current_convo.get_chat_log(NUM_CHATS) + '\n', 10) # 10 tokens for the username
        print(f'decision prediction: {response}')

    # if GPT-3 believes it should type next response, send that response
    if response and f'{botname}: ' in response:
        response = GPT_3('curie', response_training_data + current_convo.get_chat_log(NUM_CHATS) + f'\n{botname}: ')
        print('curie', response_training_data + current_convo.get_chat_log(NUM_CHATS) + f'\n{botname}: ')
        print(f'response prediction: {response}')
        async with message.channel.typing():
            typing_delay = len(response) / 15 # 15 characters per second
            print(f"Typing delay: {typing_delay}s")
            await asyncio.sleep(typing_delay)
        # await message.channel.send(f'CONVERSAITION ID: {conversation_id}\n{response}')
        await message.channel.send(response)

client.run(config["token"])
