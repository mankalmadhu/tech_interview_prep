"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/quick_sort.py until you're done.

Problem: Implement quick sort (in-place), using the
Lomuto-style partition scheme (last element as pivot).
Signature: quick_sort(arr, low, high) sorts arr[low..high] in place.

Write your solution below.
"""


def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot_index = partition(arr, low, high)
    quick_sort(arr,low, pivot_index-1)
    quick_sort(arr, pivot_index+1, high)



def partition(arr, low, high):
    pivot = arr[high]
    print(f"pivot is:{pivot}")
    i = low - 1

    for j in range(low, high):
        print(f"i is:{i}")
        if arr[j] <= pivot:
            i += 1
            print(f"swapping in loop for i:{i} and j:{j}")
            arr[i], arr[j] = arr[j], arr[i]
        print(f"inside loop:{arr}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"before return:{arr}")
    return i + 1


if __name__ == "__main__":
    # add your own test calls here once implemented
    A = [4,3,1,2]
    low = 0
    high = len(A) -1
    partition(A, low, high)
