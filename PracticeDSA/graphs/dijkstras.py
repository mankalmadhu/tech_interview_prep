import heapq
"""
Calculates the shortest path from a start node to all other nodes
in a weighted graph using Dijkstra's algorithm.

Example:
graph = {
    'S': [('A', 10), ('C', 3)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 4)],
    'C': [('A', 4), ('B', 8), ('D', 2)],
    'D': [('B', 6)],
}
distances, predecessors = find_shortest_path(graph, 'S')

Start Node: 'S'

Initial State
distances: {'S': 0, 'A': inf, 'B': inf, 'C': inf, 'D': inf}

priority_queue: [(0, 'S')]

visited: {}

predecessors: {}

Iteration 1
Pop: (0, 'S') from the priority queue.

Visit: Add 'S' to visited. visited is now {'S'}.

Neighbors of 'S':

Neighbor 'A' (weight 10): new_distance = 0 + 10 = 10. This is less than infinity.

Update distances['A'] to 10.

Update predecessors['A'] to 'S'.

Push (10, 'A') to the priority queue.

Neighbor 'C' (weight 3): new_distance = 0 + 3 = 3. This is less than infinity.

Update distances['C'] to 3.

Update predecessors['C'] to 'S'.

Push (3, 'C') to the priority queue.

End State:

distances: {'S': 0, 'A': 10, 'B': inf, 'C': 3, 'D': inf}

priority_queue: [(3, 'C'), (10, 'A')]

Iteration 2
Pop: (3, 'C') from the priority queue (it has the smallest distance).

Visit: Add 'C' to visited. visited is now {'S', 'C'}.

Neighbors of 'C':

Neighbor 'A' (weight 4): new_distance = 3 + 4 = 7. This is less than the current distances['A'] (which is 10).

Update distances['A'] to 7.

Update predecessors['A'] to 'C'.

Push (7, 'A') to the priority queue.

Neighbor 'B' (weight 8): new_distance = 3 + 8 = 11. This is less than infinity.

Update distances['B'] to 11.

Update predecessors['B'] to 'C'.

Push (11, 'B') to the priority queue.

Neighbor 'D' (weight 2): new_distance = 3 + 2 = 5. This is less than infinity.

Update distances['D'] to 5.

Update predecessors['D'] to 'C'.

Push (5, 'D') to the priority queue.

End State:

distances: {'S': 0, 'A': 7, 'B': 11, 'C': 3, 'D': 5}

priority_queue: [(5, 'D'), (7, 'A'), (10, 'A'), (11, 'B')]

Iteration 3
Pop: (5, 'D') from the priority queue.

Visit: Add 'D' to visited. visited is now {'S', 'C', 'D'}.

Neighbors of 'D':

Neighbor 'B' (weight 6): new_distance = 5 + 6 = 11. This is not less than the current distances['B'] (which is 11). No change.

End State:

priority_queue: [(7, 'A'), (10, 'A'), (11, 'B')]

Iteration 4
Pop: (7, 'A') from the priority queue.

Visit: Add 'A' to visited. visited is now {'S', 'C', 'D', 'A'}.

Neighbors of 'A':

Neighbor 'B' (weight 2): new_distance = 7 + 2 = 9. This is less than the current distances['B'] (which is 11).

Update distances['B'] to 9.

Update predecessors['B'] to 'A'.

Push (9, 'B') to the priority queue.

Neighbor 'C' (weight 1): new_distance = 7 + 1 = 8. This is not less than the current distances['C'] (which is 3). No change.

End State:

distances: {'S': 0, 'A': 7, 'B': 9, 'C': 3, 'D': 5}

priority_queue: [(9, 'B'), (10, 'A'), (11, 'B')]

Iteration 5
Pop: (9, 'B') from the priority queue.

Visit: Add 'B' to visited. visited is now {'S', 'C', 'D', 'A', 'B'}.

Neighbors of 'B':

Neighbor 'D' (weight 4): new_distance = 9 + 4 = 13. This is not less than the current distances['D'] (which is 5). No change.

End State:

priority_queue: [(10, 'A'), (11, 'B')]

Final Steps
Pop (10, 'A'): 'A' is already in visited. Skip.

Pop (11, 'B'): 'B' is already in visited. Skip.

The priority queue is now empty. The algorithm terminates.

Final Result
distances: {'S': 0, 'A': 7, 'B': 9, 'C': 3, 'D': 5}

predecessors: {'C': 'S', 'D': 'C', 'A': 'C', 'B': 'A'}


"""

def find_shortest_path(graph, start):
  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  min_priority_queue = [(0, start)]
  predecessor = {}
  visited = set()

  while min_priority_queue:
    cur_distance, cur_node = heapq.heappop(min_priority_queue)
    if cur_node in visited:
      continue
    visited.add(cur_node)
    for neighbor, weight in graph[cur_node]:
      new_distance = cur_distance + weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        predecessor[neighbor] = cur_node
        heapq.heappush(min_priority_queue, (new_distance, neighbor))

  return distances, predecessor


def get_path(predecessor, start, end):
  path = []
  cur_node = end
  while cur_node != start:
    path.append(cur_node)
    cur_node = predecessor[cur_node]
    if cur_node is None:
      return None
  path.append(start)
  path.reverse()
  return path