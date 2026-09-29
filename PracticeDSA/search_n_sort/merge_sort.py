def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Stability: when left[i] == right[j], the left element is taken
    first (since it originally preceded the right element), which
    preserves the relative order of equal elements.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    cases = [
        ([5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([2, 1], [1, 2]),
        ([3, 3, 1], [1, 3, 3]),
    ]
    for A, expected in cases:
        result = merge_sort(list(A))
        assert result == expected, f"A={A}: expected {expected}, got {result}"
        print(f"Input: {A}, Sorted: {result}")

    class _Tagged:
        """Helper to verify merge_sort is stable (compares only by key)."""

        def __init__(self, key, tag):
            self.key = key
            self.tag = tag

        def __lt__(self, other):
            return self.key < other.key

        def __gt__(self, other):
            return self.key > other.key

        def __repr__(self):
            return f"({self.key},{self.tag})"

    tagged = [_Tagged(1, "a"), _Tagged(1, "b"), _Tagged(0, "c")]
    stable_result = merge_sort(tagged)
    assert [t.tag for t in stable_result] == ["c", "a", "b"], (
        f"stability broken: {stable_result}"
    )
    print(f"Stability check passed: {stable_result}")
    print("All tests passed!")
