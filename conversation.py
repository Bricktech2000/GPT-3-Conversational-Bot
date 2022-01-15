import time

class Conversation:
    def __init__(self, conversation_timeout) -> None:
        self.people = [] # not used yet
        self.chats = [] 
        self.conversation_timeout = conversation_timeout
        self.last_chat_timestamp = time.time() # Time since last message
        self.last_fetch_timestamp = time.time() # Time since last API call

    def add_chat(self, username, message):
        if self.timed_out():
            self.chats = []
        self.chats.append(f'\n{username}: {message}')
        self.last_chat_timestamp = time.time()

    def timed_out(self):
        return self.last_chat_timestamp + self.conversation_timeout < time.time()

    def get_chat_log(self, num_chats):
        return ''.join(self.chats[-num_chats:])
