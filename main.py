import discord
import openai
import json
import sys
import asyncio

# import time
# from conversation import Conversation

# conversations = []

current_chats = []

if len(sys.argv) != 2:
    print("Usage: python main.py <training data file path>")
    exit(1)

config = json.load(open("config.json"))
training_data = open(sys.argv[1], "r").read()
client = discord.Client()
openai.api_key = config['openai_api_key']

NUM_CHATS = 10 # the number of chats to append to the training data
TEMPERATURE = 1 # the "originality" of GPT-3's answers
MAX_TOKENS = 50 # the naximal length of GPt-3's answers

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
    global current_chats

    # convo = None

    # for i in conversations:
    #     if time.time() - i.timeAlive > 5000:
    #         conversations.pop(i)
    #         continue
    #     if message.channel == i.channel:
    #         convo = i
    
    # if convo == None:
    #     convo = Conversation(message.author, message.channel, None)

    username = message.author.display_name
    username_sequence = f'{username}:'
    # https://stackoverflow.com/questions/54304428/get-bots-status-discord-py
    botname = message.guild.get_member(client.user.id).display_name
    botname_sequence = f'{botname}:'

    current_chats.append(f'\n{username_sequence} {message.content}')
    response = GPT_3(f"{training_data}{''.join(current_chats[-NUM_CHATS:-1])}\n{username_sequence} {message.content}")


    # if GPT-3 believes it should type next response, send that response
    if response and botname_sequence in response:
        response = response.replace(f'{botname_sequence} ', '')
        async with message.channel.typing():
            typing_delay = len(response) / 15 # 15 characters per second
            print(f"Typing delay: {typing_delay}s")
            await asyncio.sleep(typing_delay)
        await message.channel.send(response)

client.run(config["token"])
