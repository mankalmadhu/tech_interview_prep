
# https://www.interviewbit.com/problems/generate-all-parentheses/
class Solution:
    # @param A : string
    # @return an integer
    
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