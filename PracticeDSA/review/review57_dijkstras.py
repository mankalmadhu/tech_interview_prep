"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/graphs/dijkstras.py until you're done.

Problem (Dijkstra's Shortest Path):

Given a weighted, directed graph (adjacency dict: node -> list of
(neighbor, weight) tuples) and a start node, compute the shortest
distance from start to every other reachable node. Assume all
edge weights are non-negative.

Example:
  graph = {
      'S': [('A', 10), ('C', 3)],
      'A': [('B', 2), ('C', 1)],
      'B': [('D', 4)],
      'C': [('A', 4), ('B', 8), ('D', 2)],
      'D': [('B', 6)],
  }
  find_shortest_path(graph, 'S')
  -> {'S': 0, 'A': 7, 'B': 9, 'C': 3, 'D': 5}

Write your solution below.
"""
import heapq

def find_shortest_path(graph, start):
    min_q = [(0, start)]
    visited = set()
    distances = {node: float("inf") for node in graph.keys()}
    distances[start] = 0

    while min_q:
        cur_dist, cur_node = heapq.heappop(min_q)

        if cur_node in visited:
            continue

        visited.add(cur_node)

        if not graph.get(cur_node):
            continue

        for neighbor, weight in graph.get(cur_node):
            dist = cur_dist + weight

            if dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = dist
                heapq.heappush(min_q, (dist, neighbor))

    return distances




if __name__ == "__main__":
    graph = {
        'S': [('A', 10), ('C', 3)],
        'A': [('B', 2), ('C', 1)],
        'B': [('D', 4)],
        'C': [('A', 4), ('B', 8), ('D', 2)],
        'D': [('B', 6)],
    }
    print(find_shortest_path(graph, 'S'))
    # expect {'S': 0, 'A': 7, 'B': 9, 'C': 3, 'D': 5}

    graph2 = {0: [(1, 1)], 1: [(2, 1)], 2: []}
    print(find_shortest_path(graph2, 0))
    # expect {0: 0, 1: 1, 2: 2}

    import random

    def brute_force_shortest(graph, start):
        # Bellman-Ford style: relax all edges |V|-1 times (independent technique)
        distances = {node: float("inf") for node in graph}
        distances[start] = 0
        for _ in range(len(graph) - 1):
            updated = False
            for node, neighbors in graph.items():
                if distances[node] == float("inf"):
                    continue
                for neighbor, weight in neighbors:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
                        updated = True
            if not updated:
                break
        return distances

    for trial in range(300):
        n = random.randint(1, 15)
        nodes = list(range(n))
        graph = {node: [] for node in nodes}
        possible_edges = [(u, v) for u in nodes for v in nodes if u != v]
        random.shuffle(possible_edges)
        num_edges = random.randint(0, len(possible_edges))
        for u, v in possible_edges[:num_edges]:
            graph[u].append((v, random.randint(1, 20)))

        start = random.choice(nodes)
        got = find_shortest_path(graph, start)
        expected = brute_force_shortest(graph, start)
        assert got == expected, f"Mismatch n={n}, start={start}, graph={graph}: got {got}, expected {expected}"

    print("All stress tests passed!")
