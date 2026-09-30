"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/stacks/valid_parentheses.py until you're done.

Problem (Valid Parentheses, LeetCode 20):

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets are closed by the same type of bracket.
2. Open brackets are closed in the correct order.

Example:
  "()[]{}"  -> True
  "(]"      -> False
  "([)]"    -> False (wrong order/nesting)
  "]"       -> False (unmatched closing)

Write your solution below.
"""


class Solution:
    def isValid(self, s):
        if not s:
            return True

        stack =[]


        for ch in s:

          if self.isOpening(ch):
              stack.append(ch)
          elif stack:
              if self.isMatching(stack[-1], ch):
                  stack.pop()
              else:
                  return False
          else:
              return False


        return  len(stack) == 0

    def isValid1(self, s):
        if not s:
            return True

        stack =[]
        matching_opener_lookup = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in matching_opener_lookup:
                if stack and stack[-1] == matching_opener_lookup[ch]:
                    stack.pop()
                else :
                    return False
            else:
                stack.append(ch)



        return  len(stack) == 0




    def isMatching(self,top, input):
        matching = False

        if top == '(' and input == ')':
            matching = True
        if top == '{' and input == '}':
            matching = True
        if top == '[' and input == ']':
            matching = True

        return matching

    def isOpening(self, input):
        return input == '(' or input == '{' or input == '['



if __name__ == "__main__":
    # add your own test calls here once implemented
    s = Solution()
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid('([)]'))
    print(s.isValid(']'))

    print(s.isValid('(])'))
    print(s.isValid('}()'))

    print(s.isValid1('()[]{}'))
    print(s.isValid1('(]'))
    print(s.isValid1('([)]'))
    print(s.isValid1(']'))

    print(s.isValid1('(])'))
    print(s.isValid1('}()'))
