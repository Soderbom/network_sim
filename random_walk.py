import random
from flooding_node import FloodingNode

class RandomWalkNode(FloodingNode):
    def __init__(self, node_id, network_size, number_of_walks=2, hop_limit=4):
        super().__init__(node_id, network_size, hop_limit)
        self.number_of_walks = number_of_walks if len(self.connections) <= number_of_walks else len(connections)


    def random_walk(self):
        for msg in self.messages:
            if msg.hopcount > self.hop_limit:
                self.dropped_messages += 1
                self.messages.remove(msg)
                print(f"TTL exceeded for msg {msg.msg_id}")
                continue
            walks = random.choices(self.connections, k=self.number_of_walks)
            print(f"Walks for {self.node_id}: {walks}")
            for conn in walks:
                self.send_message(msg, conn)
        self.messages.clear()

    def handle_message(self):
        for msg in self.messages:
            if msg.dest == self.node_id:
                print(f"Node {self.node_id} recived a message with ID {msg.msg_id} from {msg.src} which was recived after {msg.hopcount} hops.")
                self.messages.remove(msg)
                self.recived_messages += 1
        self.random_walk()




