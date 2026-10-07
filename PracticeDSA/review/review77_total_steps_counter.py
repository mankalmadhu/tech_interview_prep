"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/total_steps_counter.py until you're done.

Problem (Steps by Steps (Infinite Grid)):

https://www.interviewbit.com/problems/steps-by-steps-infinite-grid/

You are on an infinite 2D grid. You're given two arrays A and B of equal
length, where (A[i], B[i]) are the coordinates of the i-th point you must
visit, in order. From any cell you can move to any of its 8 neighboring
cells (up/down/left/right/diagonals) in a single step.

Find the minimum total number of steps to visit all points in order,
starting at (A[0], B[0]).

Example:
  A = [0, 1, 1]
  B = [0, 1, 0]
  Output: 2
  (point0 -> point1: diagonal move, 1 step. point1 -> point2: move down,
   1 step. Total 2.)

Write your solution below.
"""


def cover_points(A, B):
    count = 0
    for i in range(len(A)-1):
        dx = abs(A[i] -A[i+1])
        dy = abs(B[i] - B[i+1])
        count += max(dx,dy)

    return count

if __name__ == "__main__":
    assert cover_points([0, 1, 1], [0, 1, 0]) == 2
    assert cover_points([0], [0]) == 0
    assert cover_points([0, 2, -1], [0, 2, 2]) == 2 + 3
    print("All tests passed!")

    # Stress test: compare against independent brute-force BFS on a small grid
    import random
    from collections import deque

    def bfs_steps(start, end, bound=6):
        if start == end:
            return 0
        visited = {start}
        q = deque([(start, 0)])
        while q:
            (x, y), d = q.popleft()
            for nx in range(x - 1, x + 2):
                for ny in range(y - 1, y + 2):
                    if (nx, ny) == (x, y):
                        continue
                    if abs(nx) > bound or abs(ny) > bound:
                        continue
                    if (nx, ny) == end:
                        return d + 1
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append(((nx, ny), d + 1))
        raise RuntimeError("unreachable within bound")

    for trial in range(300):
        n = random.randint(2, 5)
        A = [random.randint(-4, 4) for _ in range(n)]
        B = [random.randint(-4, 4) for _ in range(n)]
        expected = sum(
            bfs_steps((A[i], B[i]), (A[i + 1], B[i + 1]))
            for i in range(n - 1)
        )
        got = cover_points(A, B)
        assert got == expected, f"A={A}, B={B}, got={got}, expected={expected}"

    print("Stress test passed (300 trials vs BFS)!")
