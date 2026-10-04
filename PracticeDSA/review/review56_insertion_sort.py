"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/insertion_sort.py until you're done.

Problem (Insertion Sort):

Given an array of integers, sort it in ascending order using the
insertion sort algorithm (build up a sorted prefix one element at
a time, inserting each new element into its correct position).

Example:
  arr = [5, 2, 4, 6, 1, 3]
  output = [1, 2, 3, 4, 5, 6]

Write your solution below.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i-1
        while j>=0 and arr[j] > elem:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = elem

    return arr



if __name__ == "__main__":
    print(insertion_sort([5, 2, 4, 6, 1, 3]))  # expect [1,2,3,4,5,6]
    print(insertion_sort([1]))  # expect [1]
    print(insertion_sort([]))  # expect []

    import random

    for trial in range(300):
        n = random.randint(0, 100)
        arr = [random.randint(-50, 50) for _ in range(n)]
        expected = sorted(arr)
        got = insertion_sort(arr[:])
        assert got == expected, f"Mismatch on {arr}: got {got}, expected {expected}"

    print("All stress tests passed!")
