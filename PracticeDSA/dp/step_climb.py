
def climb(k):
  memo = {}
  return climb_recursive(k,memo)


def climb_recursive(k,memo):
  if k == 1 or k ==2:
    result = k
  elif k in memo:
    result = memo[k]
  else:  
    result = climb_recursive(k-1,memo) + climb_recursive(k-2,memo)
    memo[k] = result
  
  return result

def climb_tabulate(k):
  
  if k <= 2:
    return k
  dp = [0] * (k + 1)
  dp[1] = 1
  dp[2] =2 
  for i in range(3, k+1):
    dp[i] = dp[i-1] + dp[i-2]

  return dp[k]

def climb_tabulate_space_optimised(k):
  if k <= 2:
    return k
  
  one_step_before = 2
  two_step_before = 1
  current = 0

  for _ in  range(3, k+1):
    current = one_step_before + two_step_before
    two_step_before = one_step_before
    one_step_before = current

  return current
