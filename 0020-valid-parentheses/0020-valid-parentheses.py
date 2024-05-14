class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starting_brackets = ['(','[','{']
        closing_brackets  = [')',']','}']
        for item in s:
            if item in starting_brackets:
                stack.append(item)
            else:
                if len(stack)==0:
                    return False
                elif starting_brackets.index(stack[-1])!=closing_brackets.index(item):
                    return False
                else:
                    stack.pop()
        if len(stack)!=0:
            return False
        return True
                
                