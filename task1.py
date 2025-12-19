import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import defaultdict
from edges import vienna_ubahn_edges


"""------------------ TASK 1 ------------------"""

G = nx.Graph()

# ----- Add edges for all stations in all lines -----
for line, edges in vienna_ubahn_edges.items():
    for start, end, weight in edges:
        G.add_edge(start, end, weight=weight, line=line)

import networkx as nx
import matplotlib.pyplot as plt

# ----- Line colors -----
line_colors = {
    "U1": "red",
    "U2": "violet",
    "U3": "orange",
    "U4": "green",
    "U6": "brown",
}

# ----- Count number of lines for each station -----
station_lines = {}
for line, edges in vienna_ubahn_edges.items():
    for start, end, _ in edges:
        for station in [start, end]:
            if station not in station_lines:
                station_lines[station] = set()
            station_lines[station].add(line)

# ----- List of transfer stations -----
transfer_stations = [
    station for station, lines in station_lines.items() if len(lines) > 1
]


# ----- Node colors -----
node_color_dict = {}

for node in G.nodes():
    if node in transfer_stations:
        node_color_dict[node] = "yellow"  # for transfer stations
    else:
        for line, edges in vienna_ubahn_edges.items():
            if any(node == start or node == end for start, end, _ in edges):
                node_color_dict[node] = line_colors[line]
                break

# bond colors to nodes acc. to their order
node_colors = [node_color_dict[node] for node in G.nodes()]


"""------------------ TASK 2 ------------------"""


# def find_short_path(graph, start, end):
#     path = nx.shortest_path(graph, start, end, weight="weight")
#     dist = nx.shortest_path_length(graph, start, end, weight="weight")
#     print("Найкоротший шлях:", path)
#     print("Сума відстаней (км):", dist)


# start = "Stadion"
# end = "Gasometer"
# find_short_path(G, start, end)


if __name__ == "__main__":

    # ----- Visualise graph -----
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, weight="weight", seed=42, k=0.1)
    plt.title("Схема метро Відня (U-Bahn)", fontsize=18, fontweight="bold")
    line_patches = [
        mpatches.Patch(color=color, label=line) for line, color in line_colors.items()
    ]
    transfer_patch = mpatches.Patch(color="yellow", label="Пересадочні станції")
    plt.legend(handles=line_patches + [transfer_patch], loc="best")

    nx.draw(
        G,
        pos=pos,
        with_labels=True,
        node_color=node_colors,
        node_size=300,
        font_size=8,
        edge_color="gray",
    )

    plt.show()

    # ----- Analyze -----

    # Calculate degree for each station
    degree_dict = defaultdict(list)

    for node, deg in G.degree():
        degree_dict[deg].append(node)

    for deg, nodes in sorted(degree_dict.items()):
        print(f"Ступінь {deg}: {nodes}")

    # Calculate number of nodes and edges
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    print("Кількість вершин (станцій):", num_nodes)
    print("Кількість ребер (зʼєднань між станціями):", num_edges)
