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
    j = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
           j += 1
           arr[i], arr[j] =  arr[j], arr[i]
    arr[j+1],arr[high] = arr[high], arr[j+1]
    return j+1


if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
