"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/merge_sort.py until you're done.

Problem: Implement merge sort. Given a list of integers, return a
new sorted list (or sort in place — your choice) using the
divide-and-conquer merge sort algorithm.

Write your solution below.
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else :
            result.append(left[i])
            result.append(right[j])
            i +=1
            j +=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
