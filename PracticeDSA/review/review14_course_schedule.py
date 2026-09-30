"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/graphs/course_schedule.py until you're done.

Problem (Course Schedule, LeetCode 207):

There are `numCourses` courses labeled 0 to numCourses-1. You're given
`prerequisites`, a list of pairs [a, b] meaning "to take course a, you
must first take course b".

Return True if it's possible to finish all courses (i.e. no cyclic
dependency), False otherwise.

Example:
  numCourses=2, prerequisites=[[1,0]]          -> True
  numCourses=2, prerequisites=[[1,0],[0,1]]    -> False (cycle)
  numCourses=4, prerequisites=[[1,0],[2,1],[3,2]] -> True
  numCourses=4, prerequisites=[[1,0],[2,1],[3,2],[1,3]] -> False (cycle)

Write your solution below.
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj_mat = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_mat[course].append(prereq)

        global_visited = set()
        rec_visited = set()

        for course in range(numCourses):
            if self.dfs(course, adj_mat, global_visited, rec_visited):
                return False

        return True

    def dfs(self, course, adj_mat,global_visited, rec_visited):

        global_visited.add(course)
        rec_visited.add(course)

        for neighbor in adj_mat[course]:
            if neighbor not in global_visited:
                if self.dfs(neighbor, adj_mat, global_visited, rec_visited):
                    return True

            if neighbor in rec_visited:
                return True

        rec_visited.remove(course)
        return False


if __name__ == "__main__":
    # add your own test calls here once implemented
    s = Solution()
    numCourses=2
    prerequisites=[[1,0]]

    print(s.canFinish(numCourses, prerequisites))
