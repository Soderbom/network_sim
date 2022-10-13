from flooding_node import FloodingNode
from smart_broadcast import SmartBroadcastNode 
from generate_network import generate_network

def run_sim(nodes, end):
    timer = 0
    while timer < end: 
        for node in nodes:
            if len(node.messages) != 0: timer += 0.1
            node.handle_message()
        if not any([len(n.messages) != 0 for n in nodes]):
            break

def statistics(nodes):
    sent = 0
    recv = 0
    dropped = 0
    for node in nodes:
        sent += node.sent_messages
        recv += node.recived_messages
        dropped += node.dropped_messages
    print(sent, recv, dropped)

smart_nodes = generate_network("network.json", SmartBroadcastNode)
dumb_nodes = generate_network("network.json", FloodingNode)

smart_nodes[0].create_message(2)
dumb_nodes[0].create_message(2)

end = 1 
run_sim(smart_nodes, end)
input()
run_sim(dumb_nodes, end)

statistics(smart_nodes)
statistics(dumb_nodes)

