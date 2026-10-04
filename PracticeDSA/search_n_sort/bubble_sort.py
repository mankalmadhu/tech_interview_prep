def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort_opt(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    for fn in (bubble_sort, bubble_sort_opt):
        assert fn([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
        assert fn([]) == []
        assert fn([1]) == [1]
        assert fn([2, 1]) == [1, 2]
        assert fn([3, 3, 3]) == [3, 3, 3]
        assert fn([-5, 3, -1, 0]) == [-5, -1, 0, 3]
    print("fixed cases passed (both approaches)")

    import random

    for _ in range(300):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        want = sorted(nums)
        got1 = bubble_sort(nums[:])
        got2 = bubble_sort_opt(nums[:])
        assert got1 == want, f"bubble_sort: nums={nums}, expected {want}, got {got1}"
        assert got2 == want, f"bubble_sort_opt: nums={nums}, expected {want}, got {got2}"
    print("300 randomized trials passed (both approaches)")
