# import networkx as nx
from task1 import G


def dijkstra(graph, start):
    result = {vertex: [float("infinity"), []] for vertex in graph}
    if start not in result:
        return {}

    result[start] = [0, [start]]
    unvisited = list(graph)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: result[vertex][0])

        if result[current_vertex][0] == float("infinity"):
            break

        for neighbor, attrs in graph[current_vertex].items():
            distance = result[current_vertex][0] + attrs["weight"]
            if distance < result[neighbor][0]:
                result[neighbor][0] = distance
                result[neighbor][1] = result[current_vertex][1] + [neighbor]

        unvisited.remove(current_vertex)

    return result  # {vertex: [shortest_distance, [path]], ...}


if __name__ == "__main__":

    start_station = "neue donau".title()
    shortest_path = dijkstra(G, start_station)

    if not shortest_path:
        print(f"\nThere is no {start_station} station in the graph")

    else:
        for station, (shortest_distance, path) in shortest_path.items():
            print(f"\n{station.upper()}:")
            print(f"Shortest distance: {shortest_distance:.2f} km")
            print("Path:", " => ".join(path))

    ## ----- Networkx realisation -----

    # end_station = "Seestadt"

    # # ----- Dijkstra shortest path -----
    # shortest_path = nx.dijkstra_path(
    #     G, source=start_station, target=end_station, weight="weight"
    # )

    # # ----- Dijkstra shortest length -----
    # shortest_length = nx.dijkstra_path_length(
    #     G, source=start_station, target=end_station, weight="weight"
    # )

    # # ----- Shortest paths and lengths between all the nodes -----
    # all_paths = dict(nx.all_pairs_dijkstra_path(G, weight="weight"))
    # all_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight="weight"))

    # # ----- Show results -----
    # print("-" * 30)
    # print(f"Найкоротший шлях від {start_station} до {end_station} з dijkstra_path:")
    # print(shortest_path)
    # print(f"Довжина шляху (км): {shortest_length:.2f}\n{'-' * 30}")
    # print(
    #     f"Найкоротший шлях від {start_station} до {end_station} з all_pairs_dijkstra_path:"
    # )
    # print(all_paths[start_station][end_station])
    # print(f"Довжина шляху (км): {all_lengths[start_station][end_station]}\n{'-' * 30}")
