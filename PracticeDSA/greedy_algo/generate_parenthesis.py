
# https://www.interviewbit.com/problems/generate-all-parentheses/
class Solution:
    # @param A : string
    # @return an integer
    """
    Determines if the string has valid parentheses (well-formed).
        Note: Despite the filename 'generate_parenthesis', this solves 'Valid Parentheses'.

        Strategy: Stack of Expectations
        -------------------------------
        Instead of pushing the character we found (the opener) onto the stack, 
        we push the character we *expect* to see later (the closer).
        
        1. Iterate through the string.
        2. If we see an Opener ('(', '{', '['):
           - Push the corresponding Closer (')', '}', ']') onto the stack.
           - This records our "expectation".
        3. If we see a Closer:
           - It MUST match the most recent expectation (top of stack).
           - If stack is empty (unexpected closer) or top != current char (mismatch),
             return False (0).
        
        4. Final Check:
           - If the stack is empty, all expectations were met (Valid).
           - If not empty, we have unclosed openers (Invalid).

        Complexity Analysis:
        --------------------
        Time Complexity: O(N)
           - Single pass through the string.
        Space Complexity: O(N)
           - Stack stores expectations for unmatched openers.
    
    """
    
    def isValid(self, A):
        next_char_stack = []
        for ch in A:
            if ch == '(':
                next_char_stack.append(')')
            elif ch == '[':
                next_char_stack.append(']')
            elif ch == '{':
                next_char_stack.append('}')
            else:
                if (not next_char_stack) or (next_char_stack.pop() != ch) :
                    return 0

                
                continue
        
        return 1 if not next_char_stack else 0