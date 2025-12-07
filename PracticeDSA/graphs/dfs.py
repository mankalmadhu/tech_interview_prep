
def dfs(graph, start_node):
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