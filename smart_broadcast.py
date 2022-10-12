import random
from message import Message
from flooding_node import FloodingNode

class SmartBroadcastNode(FloodingNode):
    def __init__(self, node_id, hop_limit=4):
        FloodingNode.__init__(self, node_id)
        self.memory_size = 100
        self.seen_messages = [-1] * self.memory_size


    def handle_message(self):
        for msg in self.messages:
            if msg.hopcount > self.hop_limit:
                self.dropped_messages += 1
                self.messages.remove(msg)
                continue

            has_seen = self.seen_messages[msg.msg_id % self.memory_size] == msg.msg_id
            if not has_seen:
                self.seen_messages[msg.msg_id % self.memory_size] = msg.msg_id
                if msg.dest == self.node_id:
                    print(f"Node {self.node_id} recived a message with ID {msg.msg_id} from {msg.src} which was recived after {msg.hopcount} hops ::: {msg}.")
                    self.recived_messages += 1
                    self.messages.remove(msg)

                    print("Creating new message")
                    self.create_message()
            else:
                print(f"Node_{self.node_id} has already processed message with ID:{msg.msg_id}. Deleting")
                self.messages.remove(msg)


        self.broadcast()
