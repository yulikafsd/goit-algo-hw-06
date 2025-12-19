from task1 import G
import networkx as nx


if __name__ == "__main__":

    start_station = "Stephansplatz"
    end_station = "Seestadt"

    # ----- Dijkstra shortest path -----
    shortest_path = nx.dijkstra_path(
        G, source=start_station, target=end_station, weight="weight"
    )

    # ----- Dijkstra shortest length -----
    shortest_length = nx.dijkstra_path_length(
        G, source=start_station, target=end_station, weight="weight"
    )

    # ----- Shortest paths and lengths between all the nodes -----
    all_paths = dict(nx.all_pairs_dijkstra_path(G, weight="weight"))
    all_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight="weight"))

    # ----- Show results -----
    print("-" * 30)
    print(f"Найкоротший шлях від {start_station} до {end_station} з dijkstra_path:")
    print(shortest_path)
    print(f"Довжина шляху (км): {shortest_length:.2f}\n{'-' * 30}")
    print(
        f"Найкоротший шлях від {start_station} до {end_station} з all_pairs_dijkstra_path:"
    )
    print(all_paths[start_station][end_station])
    print(f"Довжина шляху (км): {all_lengths[start_station][end_station]}\n{'-' * 30}")
