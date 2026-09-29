def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot_index = partition(arr, low, high)
    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    cases = [
        [5, 3, 1, 4, 2],
        [1],
        [],
        [2, 1],
        [3, 3, 1],
        [3, 1, 2],
        [1, 3, 2],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1],
    ]
    for A in cases:
        expected = sorted(A)
        result = list(A)
        quick_sort(result, 0, len(result) - 1)
        assert result == expected, f"A={A}: expected {expected}, got {result}"
        print(f"Input: {A}, Sorted: {result}")
    print("All tests passed!")
