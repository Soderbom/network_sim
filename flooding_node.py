import random
from message import Message

class FloodingNode:
    def __init__(self, node_id, network_size, hop_limit=4):
        self.node_id = node_id 
        self.connections = [] 
        self.messages = [] 
        self.network_size = network_size
        self.hop_limit = hop_limit

        # Statistic
        self.sent_messages = 0
        self.recived_messages = 0
        self.dropped_messages = 0

    def create_message(self, dest=-1):
        src = self.node_id 

        # Om en destination inte har angets, slumpa ett nod ID
        if dest == -1:
            dest = random.randint(0, self.network_size-1)
            while dest == self.node_id:
                dest = random.randint(0, self.network_size-1)
        
        new_msg = Message(src, dest)
        self.messages.append(new_msg)

    def send_message(self, msg, connection):
        msg_copy = msg.copy()
        print(f"Node_{self.node_id}->Node_{connection.node_id}: Sending message with dest: Node_{msg.dest} with ID:{msg_copy.msg_id} ::: {msg_copy}")
        msg_copy.hopcount += 1
        connection.messages.append(msg_copy)
        self.sent_messages += 1

    def broadcast(self):
        for msg in self.messages:
            for connection in self.connections:
                self.send_message(msg, connection)
        self.messages.clear()

    def handle_message(self):
        for msg in self.messages:
            if msg.hopcount > self.hop_limit:
                self.dropped_messages += 1
                self.messages.remove(msg)
                print("TTL exceeded")
                continue
            if msg.dest == self.node_id:
                print(f"Node {self.node_id} recived a message with ID {msg.msg_id} from {msg.src} which was recived after {msg.hopcount} hops.")
                self.messages.remove(msg)
                self.recived_messages += 1
            else:
                self.broadcast()




