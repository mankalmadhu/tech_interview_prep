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


def find_shortest_path(graph, start):
    pass


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
