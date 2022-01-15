import time

class Timer:
    def __init__(self):
        self.storedTime = time.time()

    def Restart(self):
        self.storedTime = time.time()

    def Current_Length(self):
        """Returns float of time since last restart"""
        return time.time() - self.storedTime

# maxTime = Timer()

# maxTime.Restart()

# print(maxTime.Current_Length())