import random
import time

class Message:
    def __init__(self, src, dest):
        random.seed(time.time())

        self.src = src
        self.dest = dest
        self.msg_id = random.randint(0, 65000)
        self.hopcount = 0

    def copy(self):
        msg_copy = Message(self.src, self.dest)
        msg_copy.msg_id = self.msg_id
        msg_copy.hopcount = self.hopcount

        return msg_copy
