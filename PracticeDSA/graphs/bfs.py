from collections import deque

def bfs(graph, start):
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
  