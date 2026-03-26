import matplotlib.pyplot as plt

import networkx as nx

# create graph
G = nx.DiGraph()

# define layers (number of neurons in each layer)
layers = [8, 10, 6,7,11]  # input, hidden, output

pos = {}
node_id = 0
layer_nodes = []

# create neurons
for layer_index, num_neurons in enumerate(layers):
    current_layer = []
    for i in range(num_neurons):
        G.add_node(node_id)
        pos[node_id] = (layer_index, -i)  # x = layer, y = neuron position
        current_layer.append(node_id)
        node_id += 1
    layer_nodes.append(current_layer)

# create connections between layers
for i in range(len(layer_nodes) - 1):
    for n1 in layer_nodes[i]:
        for n2 in layer_nodes[i + 1]:
            G.add_edge(n1, n2)

# draw network
plt.figure(figsize=(6,4))
nx.draw(
    G,
    pos,
    with_labels=False,
    node_color="skyblue",
    node_size=800,
    arrows=False
)

plt.title("Simple Neural Network Visualization")
plt.show()
