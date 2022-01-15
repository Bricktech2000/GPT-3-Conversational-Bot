import time

class Conversation:
    def __init__(self, conversation_timeout, time_delay) -> None:
        self.people = [] # not used yet
        self.chats = [] 
        self.conversation_timeout = conversation_timeout
        self.time_delay = time_delay
        self.last_chat_timestamp = time.time() # Time since last message

    def add_chat(self, username, message):
        if self._timed_out():
            self.chats = []
        self.chats.append(f'\n{username}: {message}')
        self.last_chat_timestamp = time.time()

    def _timed_out(self):
        return self.last_chat_timestamp + self.conversation_timeout < time.time()
    
    def should_fetch(self):
        return self.last_chat_timestamp + self.time_delay < time.time()

    def get_chat_log(self, num_chats):
        return ''.join(self.chats[-num_chats:])
