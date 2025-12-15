from collections import deque

def bfs(graph, start):
  """
        Performs Breadth-First Search (BFS) on a graph.

        Strategy: Level-Order Traversal using a Queue
        ---------------------------------------------
        BFS explores the graph layer by layer, starting from the source.
        
        1. Data Structure: Queue (Deque).
           - Essential for maintaining the FIFO order required to process 
             all neighbors of depth 'd' before any node at depth 'd+1'.
        2. Visited Set:
           - Keeps track of visited nodes to prevent cycles and redundant processing.
        
        Algorithm:
        - Push 'start' to queue and mark visited.
        - While queue is not empty:
          - Pop node from LEFT (oldest).
          - Add unvisited neighbors to RIGHT (newest) and mark them visited immediately.

        Complexity Analysis:
        --------------------
        Time Complexity: O(V + E)
           - We visit every Vertex (V) once.
           - We iterate over every Edge (E) associated with those vertices.
        
        Space Complexity: O(V)
           - To store the visited set and the queue (which can hold up to V nodes 
             in the worst case, e.g., a star graph).
        """
  visited = set([start])
  queue = deque([start])
  result = []

  while queue:
    cur_node = queue.popleft()
    result.append(cur_node)
    for neighbor in graph[cur_node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

  return result
  