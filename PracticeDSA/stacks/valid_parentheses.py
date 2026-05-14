class Solution:
    """
    Validates if a string of parentheses is properly closed and nested.
    
    Time Complexity: O(N)
    - We iterate through the string exactly once.
    - Dictionary lookups and Stack push/pop operations are O(1).
    
    Space Complexity: O(N)
    - In the worst case (e.g., all opening brackets "((((("), the stack will
      store all N characters.
      
    Logic:
    - Use a Stack to track opening brackets.
    - If we see an opening bracket, push it to the stack.
    - If we see a closing bracket:
      - Check if the stack is empty (if so, it's an unmatched closing bracket).
      - Check if the top of the stack matches the correct opening bracket.
      - If it matches, pop it. If not, immediately return False.
    - At the end, the stack must be completely empty to be valid.
    """
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in bracket_map:
                if stack and stack[-1] == bracket_map[i]:
                    stack.pop()
                else:
                    return False        
            else:
                stack.append(i)
                
        return len(stack) == 0

if __name__ == '__main__':
    sol = Solution()
    print("Test 1: ()[]{} -> Expected: True, Got:", sol.isValid("()[]{}"))
    print("Test 2: (]     -> Expected: False, Got:", sol.isValid("(]"))
    print("Test 3: ([)]   -> Expected: False, Got:", sol.isValid("([)]"))
    print("Test 4: ]      -> Expected: False, Got:", sol.isValid("]"))
    print("All tests executed!")
