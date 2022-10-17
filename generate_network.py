from flooding_node import FloodingNode
from smart_broadcast import SmartBroadcastNode 
from random_walk import RandomWalkNode
import json

def generate_network(file, NodeType, hop_limit=4, walks=0):
    with open(file) as f:
        network = json.load(f)
    if walks:
        nodes = [NodeType(i, len(network), hop_limit=hop_limit, number_of_walks=walks) for i in range(len(network))]
    else:
        nodes = [NodeType(i, len(network), hop_limit=hop_limit) for i in range(len(network))]

    for node, conn_list in network.items():
        for conn in conn_list:
            nodes[int(node)].connections.append(nodes[conn])

    return nodes

if __name__ == "__main__":
    file = "network.json"
    flood = generate_network(file, FloodingNode)
    smart = generate_network(file, SmartBroadcastNode)
    rnode = generate_network(file, RandomWalkNode, 1)

    for f in flood:
        print(f.connections)

    for s in smart:
        print(s.connections)

    for r in rnode:
        print(r.connections)
