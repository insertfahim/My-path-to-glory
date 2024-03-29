class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            values = []
            if token not in ["+", "-", "*", "/"]:
                numbers.append(int(token))
            else:
                values.append(numbers.pop())
                values.append(numbers.pop())
                res = None
                if token=='*':
                    res = values[0]*values[1]
                elif token=='/':
                    res = int(values[1]/values[0])
                elif token=='+':
                    res = values[0]+values[1]
                elif token=='-':
                    res = values[1]-values[0]
                numbers.append(res)
        return numbers[0]
        