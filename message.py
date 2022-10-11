import random
import time

class Message:
    def __init__(self, src, dest):
        random.seed(time.time())

        self.src = src
        self.dest = dest
        self.msg_id = random.randint(0, 65000)
        self.hopcount = 0