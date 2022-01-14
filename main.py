import discord
import openai
import json
import asyncio

# import time
# from conversation import Conversation


conversations = []
current_chats = []

config = json.load(open("config.json"))
bot_sequence = "Grace:"
training_data = open("session_prompt.txt", "r").read()
training_data = training_data.replace('Bot: ', 'Grace: ') # temporary hack
client = discord.Client()
openai.api_key = config['openai_api_key']

NUM_CHATS = 4

def GPT_3(chat_log):
    print('\n\n\n\n', chat_log)
    response = openai.Completion.create(
        engine="curie",
        prompt=chat_log + '\n',
        temperature=0.8,
        max_tokens=75,
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

    # if message.author.bot: return

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

    current_chats.append(f'\n{username_sequence} {message.content}')
    response = GPT_3(f"{training_data}{''.join(current_chats[-NUM_CHATS:-1])}\n{username_sequence} {message.content}")
    

    if response and bot_sequence in response:
        response = response.replace(f'{bot_sequence} ', '')
        # current_chats.append(f'\n{bot_sequence} {response}')
        # https://stackoverflow.com/questions/62311644/discord-py-how-to-display-bot-typing-indicator-in-dms
        # https://stackoverflow.com/questions/64826460/how-do-i-make-discord-bot-display-typing-and-stop-typing-when-a-message-is-sent
        async with message.channel.typing():
            await asyncio.sleep(0.5)
        await message.channel.send(response)

client.run(config["token"])
