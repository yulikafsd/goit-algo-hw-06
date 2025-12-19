from collections import deque
from task1 import G


# ----- DFS -----
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            # Calculate length of the path
            length = sum(
                graph[path[i]][path[i + 1]]["weight"] for i in range(len(path) - 1)
            )
            return path, length
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None, None


# ----- BFS -----
def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            length = sum(
                graph[path[i]][path[i + 1]]["weight"] for i in range(len(path) - 1)
            )
            return path, length
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append(path + [neighbor])
    return None, None


if __name__ == "__main__":
    start_station = "Stephansplatz"
    end_station = "Seestadt"

    dfs_result, dfs_length = dfs_path(G, start_station, end_station)
    bfs_result, bfs_length = bfs_path(G, start_station, end_station)

    print("-" * 30)
    print(f"DFS шлях від {start_station} до {end_station}:")
    print(dfs_result)
    print(f"Довжина шляху (км): {dfs_length:.2f}\n{'-' * 30}")

    print(f"BFS шлях від {start_station} до {end_station}:")
    print(bfs_result)
    print(f"Довжина шляху (км): {bfs_length:.2f}\n{'-' * 30}")
