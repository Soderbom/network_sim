from flooding_node import FloodingNode

node_a = FloodingNode(0)
node_b = FloodingNode(1)
node_c = FloodingNode(2)

nodes = [node_a, node_b, node_c]

node_a.connections.append(node_b)
node_b.connections.append(node_a)
node_b.connections.append(node_c)
node_c.connections.append(node_b)

node_a.create_message()

timer = 0
end = 3600

while timer < end:
    timer += 0.1
    for node in nodes:
        node.clean_message_list()
        node.handle_message()


 
