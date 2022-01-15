import time

class Conversation:
    def __init__(self, timeAlive=time.time()) -> None:
        self.people = [] # not used yet
        self.timeAlive = timeAlive # length of convo, has the option to be set because of no_convo in main
        self.chats = [] 
        self.storedTime = time.time() # Time since last message
    
    def Add_Chat(self, username, message):
        self.chats.append(f"\n{username} {message}")

    def Restart_Timer(self):
        self.storedTime = time.time()

    def Current_Length(self):
        """Returns float of time since last restart"""
        return time.time() - self.storedTime