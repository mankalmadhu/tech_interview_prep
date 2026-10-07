class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    # https://www.interviewbit.com/problems/steps-by-steps-infinite-grid/

    def coverPoints(self, A, B):
        total_counts = 0
        for i in range(len(A) - 1):
            dx = abs(A[i] - A[i + 1])
            dy = abs(B[i] - B[i + 1])
            total_counts += max(dx, dy)

        return total_counts


if __name__ == "__main__":
    import random
    from collections import deque

    sol = Solution()

    assert sol.coverPoints([0, 1, 1], [0, 1, 0]) == 2
    assert sol.coverPoints([0], [0]) == 0
    assert sol.coverPoints([0, 2, -1], [0, 2, 2]) == 2 + 3

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

    for _ in range(300):
        n = random.randint(2, 5)
        A = [random.randint(-4, 4) for _ in range(n)]
        B = [random.randint(-4, 4) for _ in range(n)]
        expected = sum(
            bfs_steps((A[i], B[i]), (A[i + 1], B[i + 1]))
            for i in range(n - 1)
        )
        got = sol.coverPoints(A, B)
        assert got == expected, f"A={A}, B={B}, got={got}, expected={expected}"

    print("All tests passed!")
