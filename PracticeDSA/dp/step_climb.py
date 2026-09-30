def climb(k):
    memo = {}
    return climb_recursive(k, memo)


def climb_recursive(k, memo):
    if k == 1 or k == 2:
        result = k
    elif k in memo:
        result = memo[k]
    else:
        result = climb_recursive(k - 1, memo) + climb_recursive(k - 2, memo)
        memo[k] = result

    return result


def climb_tabulate(k):

    if k <= 2:
        return k
    dp = [0] * (k + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, k + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[k]


def climb_tabulate_space_optimised(k):
    if k <= 2:
        return k

    one_step_before = 2
    two_step_before = 1
    current = 0

    for _ in range(3, k + 1):
        current = one_step_before + two_step_before
        two_step_before = one_step_before
        one_step_before = current

    return current


if __name__ == "__main__":
    fixed_cases = [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (10, 89)]
    for k, expected in fixed_cases:
        for fn in (climb, climb_tabulate, climb_tabulate_space_optimised):
            got = fn(k)
            assert got == expected, f"{fn.__name__}({k}) = {got}, expected {expected}"
    print(f"All {len(fixed_cases)} fixed cases passed for all 3 implementations.")

    import time

    start = time.time()
    climb(500)
    elapsed = time.time() - start
    assert elapsed < 0.01, (
        f"climb(500) took {elapsed:.4f}s -- memoization may be broken"
    )
    print(f"climb(500) ran in {elapsed:.6f}s -- memoization confirmed working.")
