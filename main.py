import discord
import openai
import json

# import time
# from conversation import Conversation


conversations = []
current_chats = []

config = json.load(open("config.json"))
bot_sequence = "\nBot:"
training_data = open("session_prompt.txt", "r").read()
client = discord.Client()
openai.api_key = config['openai_api_key']

NUM_CHATS = 10

def ask(question, username_sequence, chat_log=None):
    prompt_text = f'{chat_log}{username_sequence} {question}\n'
    print('\n\n\n\n', prompt_text, end='')
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
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
    username_sequence = f'\n{username}:'

    current_chats.append(f'{username_sequence} {message.content}')
    response = ask(message.content, username_sequence, training_data + ''.join(current_chats[-NUM_CHATS:-1]))

    if response and "Bot: " in response:
        response = response.replace("Bot: ", "")
        current_chats.append(f'{bot_sequence} {response}')
        await message.channel.send(response)

client.run(config["token"])
