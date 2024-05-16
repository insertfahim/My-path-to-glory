class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                if token=='+':
                    stack.append(stack.pop()+stack.pop())
                elif token=='-':
                    second_value = stack.pop()
                    first_value  = stack.pop()
                    stack.append(first_value-second_value)
                elif token=='*':
                    stack.append(stack.pop()*stack.pop())
                elif token=='/':
                    second_value = stack.pop()
                    first_value  = stack.pop()
                    stack.append(int(first_value/second_value))
        return stack[0]