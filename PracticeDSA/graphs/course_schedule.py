class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Determines if all courses can be finished given prerequisites.

        Algorithm: Depth-First Search (DFS) Cycle Detection (3-State)
        - Time Complexity: O(V + E) where V is numCourses and E is prerequisites.
          Every node and edge is visited at most once due to the `visited` set.
        - Space Complexity: O(V + E) to store the adjacency list, plus O(V) for 
          the recursion stack and visited sets.

        Logic:
        - `visited` tracks all nodes that have been fully processed and proven cycle-free.
        - `recursion_stack` tracks nodes currently being explored in the active DFS path.
        - If we encounter a neighbor already in `recursion_stack`, a cycle exists.
        - Optimization: We can also set `prereqs[course] = []` right before returning 
          False in DFS to instantly prune future redundant checks.

        Cycle Trace Example (1 -> 0, 0 -> 1):
        - Start DFS(1): Add 1 to `visited` and `recursion_stack`.
        - Check neighbors of 1 (which is 0).
        - Start DFS(0): Add 0 to `visited` and `recursion_stack`.
        - Check neighbors of 0 (which is 1).
        - Neighbor 1 is already in `recursion_stack`!
        - Cycle detected -> Returns True immediately.
        """
        
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        recursion_stack = set()

        for course in range(numCourses):
            if course not in visited:
                if self.dfs(course, adj, visited, recursion_stack):
                    return False
        return True

    def dfs(self, course, prereqs, visited, recursion_stack):
        visited.add(course)
        recursion_stack.add(course)
        
        for neighbor in prereqs[course]:
            if neighbor not in visited:
                if self.dfs(neighbor, prereqs, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True
        
        recursion_stack.remove(course)
        return False


if __name__ == '__main__':
    sol = Solution()
    print("Test 1: 2 courses, [[1,0]]         -> Expected: True, Got:", sol.canFinish(2, [[1,0]]))
    print("Test 2: 2 courses, [[1,0],[0,1]]   -> Expected: False, Got:", sol.canFinish(2, [[1,0],[0,1]]))
    print("Test 3: 4 courses, [[1,0],[2,1],[3,2]] -> Expected: True, Got:", sol.canFinish(4, [[1,0],[2,1],[3,2]]))
    print("Test 4: 4 courses, [[1,0],[2,1],[3,2],[1,3]] -> Expected: False, Got:", sol.canFinish(4, [[1,0],[2,1],[3,2],[1,3]]))
    print("All tests executed!")
