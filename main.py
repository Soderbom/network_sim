from flooding_node import FloodingNode
from smart_broadcast import SmartBroadcastNode 
from generate_network import generate_network
from random_walk import RandomWalkNode

def run_sim(nodes):
    while True: 
        for node in nodes:
            node.handle_message()
        if not any([len(n.messages) != 0 for n in nodes]):
            return


def statistics(nodes):
    sent = 0
    recv = 0
    dropped = 0
    for node in nodes:
        sent += node.sent_messages
        recv += node.recived_messages
        dropped += node.dropped_messages
    return sent, recv, dropped



limit = 4

smart_nodes = generate_network("network.json", SmartBroadcastNode, hop_limit=limit)
dumb_nodes = generate_network("network.json", FloodingNode, hop_limit=limit)
random_nodes = generate_network("network.json", RandomWalkNode,  hop_limit=limit, walks=2)

smart_nodes[0].create_message(8)
dumb_nodes[0].create_message(8)
random_nodes[0].create_message(8)

run_sim(smart_nodes)
run_sim(random_nodes)
run_sim(dumb_nodes)

print(f"Dumb nodes: {statistics(dumb_nodes)}")
print(f"Smart nodes: {statistics(smart_nodes)}")
print(f"Random nodes: {statistics(random_nodes)}")

