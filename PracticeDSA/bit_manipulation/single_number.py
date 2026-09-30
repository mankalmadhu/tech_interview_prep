# https://www.interviewbit.com/problems/single-number/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for num in A:
            result ^= num

        return result


if __name__ == "__main__":
    import random

    fixed_cases = [
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([-5, 3, -5], 3),
        ([0, 0, 7], 7),
    ]
    for A, expected in fixed_cases:
        got = Solution().singleNumber(A)
        assert got == expected, f"singleNumber({A}) = {got}, expected {expected}"
    print(f"All {len(fixed_cases)} fixed cases passed.")

    random.seed(13)
    for _ in range(2000):
        n = random.randint(1, 20)
        pool = random.sample(range(-50, 50), n)
        single = pool[0]
        A = pool[1:] * 2 + [single]
        random.shuffle(A)
        got = Solution().singleNumber(A)
        assert got == single, f"singleNumber({A}) = {got}, expected {single}"
    print("2000 randomized stress trials passed.")
