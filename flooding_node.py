import random
from message import Message

class FloodingNode:
    def __init__(self, node_id):
        self.node_id = node_id 
        self.connections = [] 
        self.messages = [] 
        self.sent_messages = 0
        self.recived_messages = 0

    def clean_message_list(self):
        for msg in self.messages:
            if msg.hopcount > 4:
                self.messages.remove(msg)

    def create_message(self):
        src = self.node_id 
        dest = random.choice(self.connections).node_id 
        new_msg = Message(src, dest)
        self.messages.append(new_msg)

    def send_message(self, msg, connection):
        connection.messages.append(msg)
        msg.hopcount += 1
        self.sent_messages += 1

    def broadcast(self):
        for msg in self.messages:
            for connection in self.connections:
                self.send_message(msg, connection)
        self.messages.clear()

    def handle_message(self):
        for msg in self.messages:
            dest = msg.dest
            if dest == self.node_id:
                print(f"Node {self.node_id} recived a message with ID {msg.msg_id} from {msg.src} which was recived after {msg.hopcount} hops.")
                self.messages.remove(msg)
                self.recived_messages += 1

                self.create_message()
                self.broadcast()
            else:
                self.broadcast()




