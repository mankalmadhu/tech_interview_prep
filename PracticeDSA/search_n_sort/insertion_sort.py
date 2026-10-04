def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    for arr in ([5, 2, 4, 6, 1, 3], [1], []):
        copy = arr[:]
        insertion_sort(copy)
        print(copy)

    import random

    for trial in range(300):
        n = random.randint(0, 100)
        arr = [random.randint(-50, 50) for _ in range(n)]
        expected = sorted(arr)
        insertion_sort(arr)
        assert arr == expected, f"Mismatch: got {arr}, expected {expected}"

    print("All stress tests passed!")
