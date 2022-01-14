import time

class Conversation:
    def __init__(self, people, channel, mood) -> None:
        self.people = people # array of people in convo
        self.channel = channel
        self.mood = mood # what
        self.timeAlive = time.time()