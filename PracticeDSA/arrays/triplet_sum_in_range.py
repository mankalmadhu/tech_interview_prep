class Solution:
    # @param A : list of strings
    # @return an integer
    # https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/

    def solve(self, A):
        n = len(A)
        if n < 3:
            return 0

        a_max1, a_max2, a_max3 = float('-inf'), float('-inf'), float('-inf')
        a_min1, a_min2 = float('inf'), float('inf')
        b_max1, b_max2 = float('-inf'), float('-inf')
        b_min1 = float('inf')
        c_min1 = float('inf')

        for i in range(n):
            num = float(A[i])
            if num < 2 / 3:
                a_min1, a_min2 = self.get_abucket_min(num, a_min1, a_min2)
                a_max1, a_max2, a_max3 = self.get_abucket_max(
                    num, a_max1, a_max2, a_max3)
            elif num >= 2 / 3 and num < 1:
                b_min1 = self.get_bbucket_min(num, b_min1)
                b_max1, b_max2 = self.get_bbucket_max(num, b_max1, b_max2)
            elif num >= 1 and num < 2:
                c_min1 = self.get_cbucket_min(num, c_min1)

        #combine the print statements into one line
        print(
            f"a_min1: {a_min1}, a_min2: {a_min2}, a_max1: {a_max1}, a_max2: {a_max2}, a_max3: {a_max3}, b_min1: {b_min1}, b_max1: {b_max1}, b_max2: {b_max2}, c_min1: {c_min1}"
        )

        comb1 = self.is_in_range(a_max1, a_max2, a_max3)
        comb2 = self.is_in_range(a_max2, a_max3, b_max2)
        comb3 = self.is_in_range(a_min1, a_min2, c_min1)
        comb4 = self.is_in_range(a_min1, b_max1, b_max2)
        comb5 = self.is_in_range(a_min1, b_min1, c_min1)

        # pretty print with variable names and values all comb values
        print(
            f"comb1: {comb1}, comb2: {comb2}, comb3: {comb3}, comb4: {comb4}, comb5: {comb5}"
        )

        return 1 if (comb1 or comb2 or comb3 or comb4 or comb5) else 0

    def is_in_range(self, a, b, c):

        import math
        if math.isinf(a) or math.isinf(b) or math.isinf(c):
            return False

        sum = a + b + c
        return sum > 1 and sum < 2

    def get_abucket_min(self, num, min1, min2):

        if num < min1:
            min1, min2 = num, min1
        elif num < min2:
            min2 = num

        return min1, min2

    def get_abucket_max(self, num, max1, max2, max3):
        if num > max3:
            max3, max2, max1 = num, max3, max2
        elif num > max2:
            max2, max1 = num, max2
        elif num > max1:
            max1 = num
        return max1, max2, max3

    def get_bbucket_min(self, num, min1):
        if num < min1:
            min1 = num

        return min1

    def get_bbucket_max(self, num, max1, max2):
        if num > max2:
            max2, max1 = num, max2
        elif num > max1:
            max1 = num
        return max1, max2

    def get_cbucket_min(self, num, min1):
        if num < min1:
            min1 = num
        return min1

    def solve_two_pointer(self, A):

        A = sorted([float(s) for s in A])
        n = len(A)
        for i in range(n):
            if A[i] >= 2:
                break
            left = i + 1
            right = n - 1
            while left < right:
                sum = A[i] + A[left] + A[right]
                if sum > 1 and sum < 2:
                    return 1
                elif sum <= 1:
                    left += 1
                else:
                    right -= 1

        return 0


def main():
    inputs = [["0.6", "0.7", "0.8", "1.2", "0.4"], ["0.1", "0.2", "0.3", "0.4"],
        ["0.8", "0.7", "0.9"], ["0.1", "0.8", "0.25", "1.5"],
        ["0.2", "0.3", "2.5", "3.0"], ["1.1", "0.5"],
        [
            "2.673662", "2.419159", "0.573816", "2.454376", "0.403605",
            "2.503658", "0.806191"
        ]]

    expected_outputs = [1, 0, 0, 1, 0, 0, 1]

    for idx, A in enumerate(inputs):
        sol = Solution()
        result = sol.solve(A)
        print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
    