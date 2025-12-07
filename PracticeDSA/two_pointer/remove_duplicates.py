class Solution:

    def removeDuplicates(self, A):
        """
        Key line here is the  A[low] = A[high] inside not equal check.
        In case of not equal scneario only hihg is incremented and low is not incremented.
        Effecitively in case of equal scneario, the repeated elemtns are glossed over, eliminating duplicates.
        """
        low = 0
        high = 1
        n = len(A)

        while high < n:
            if A[low] != A[high]:
                low += 1
                A[low] = A[high]
            high += 1
        for i in range(low + 1, n):
            A[i] = -1
        return low + 1


if __name__ == "__main__":
    sol = Solution()
    As = [[1, 1, 2], [1, 2, 2, 3, 3]]
    expected = [2, 3]
    for i in range(len(As)):

        result = sol.removeDuplicates(As[i])
        print(f'result:{result},expected:{expected[i]}')
