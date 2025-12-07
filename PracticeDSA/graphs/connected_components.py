from collections import deque


def connected_components(graph):
  visited = set()
  count = 0

  for node in graph:
    if node not in visited:
      count += 1
      visited.add(node)
      __bfs(graph, node, visited)

  return count


def __bfs(graph, start, visited):
  queue = deque([start])

  while queue:
    cur_node = queue.popleft()
    for neighbor in graph[cur_node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
