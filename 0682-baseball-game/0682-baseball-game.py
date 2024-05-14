class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for ops in operations:
            # if 64<=ord(ops)<=73:
            #     record.append(int(ops))
            if ops=='+':
                record.append(sum(record[-1:-3:-1]))
            elif ops=='D':
                record.append(record[-1]*2)
            elif ops=='C':
                record.pop()
            else:
                record.append(int(ops))
        return sum(record)
        