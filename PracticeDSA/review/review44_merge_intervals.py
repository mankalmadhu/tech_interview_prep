"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/merge_intervals.py until you're done.

Problem (Merge Intervals, LeetCode 56):

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.

Example:
  intervals = [[1,3],[2,6],[8,10],[15,18]]
  output = [[1,6],[8,10],[15,18]]
  (since [1,3] and [2,6] overlap, merge into [1,6])

Write your solution below.
"""


def merge_intervals(intervals):
    merged_list = []

    if not intervals:
        return merged_list

    intervals.sort(key=lambda x: x[0])
    merged_list.append(intervals[0])

    for i in range(1, len(intervals)):
        cur_start, cur_end = intervals[i]
        _, prev_end = merged_list[-1]

        if cur_start <= prev_end:
            merged_list[-1][1] = max(prev_end, cur_end)
        else:
            merged_list.append(intervals[i])

    return merged_list




if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # expect [[1,6],[8,10],[15,18]]
    print(merge_intervals([[1, 4], [4, 5]]))  # expect [[1,5]]

    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([]) == []
    assert merge_intervals([[1, 4]]) == [[1, 4]]
    assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]  # fully contained
    print("fixed cases passed")

    import random

    def brute_force(intervals):
        # independent approach: build a graph where intervals are nodes,
        # connect overlapping/touching pairs, then merge each connected
        # component into [min start, max end].
        n = len(intervals)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for i in range(n):
            for j in range(i + 1, n):
                s1, e1 = intervals[i]
                s2, e2 = intervals[j]
                if s1 <= e2 and s2 <= e1:
                    union(i, j)

        groups = {}
        for i in range(n):
            root = find(i)
            groups.setdefault(root, []).append(intervals[i])

        merged = []
        for group in groups.values():
            start = min(s for s, _ in group)
            end = max(e for _, e in group)
            merged.append([start, end])

        merged.sort(key=lambda x: x[0])
        return merged

    for _ in range(300):
        n = random.randint(0, 10)
        intervals = []
        for _ in range(n):
            a = random.randint(0, 20)
            b = random.randint(0, 20)
            intervals.append([min(a, b), max(a, b)])
        got = merge_intervals([iv[:] for iv in intervals])
        want = brute_force(intervals)
        assert got == want, f"intervals={intervals}: expected {want}, got {got}"
    print("300 randomized trials passed")
