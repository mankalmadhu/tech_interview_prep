
def dfs(graph, start_node):
  """
        Performs Depth-First Search (DFS) on a graph.

        Strategy: Recursive Traversal
        -----------------------------
        DFS explores as far as possible along each branch before backtracking.
        
        1. Visited Set: 
           - Tracks nodes to prevent processing cycles or redundant visits.
        2. Recursion (Implicit Stack):
           - Instead of an explicit stack data structure, we rely on the 
             Call Stack of the program to manage the backtracking order.
        
        Algorithm:
        - Mark current 'node' as visited and add to result.
        - For each neighbor:
          - If not visited, recursively call dfs on that neighbor.
          - This "pauses" the current node's loop until the neighbor returns.

        Complexity Analysis:
        --------------------
        Time Complexity: O(V + E)
           - We visit every Vertex (V) once.
           - We check every Edge (E) exactly twice (once from each end).
        
        Space Complexity: O(V)
           - Visited set stores O(V) nodes.
           - Recursion Stack depth can go up to O(V) in the worst case 
             (e.g., a straight line graph).
        """
  visited = set()
  result = []
  __dfs_recursive(graph, start_node, visited, result)
  return result


def __dfs_recursive(graph, node, visited, result):
  visited.add(node)
  result.append(node)
  for neighbor in graph[node]:
    if neighbor not in visited:
      __dfs_recursive(graph, neighbor, visited, result)