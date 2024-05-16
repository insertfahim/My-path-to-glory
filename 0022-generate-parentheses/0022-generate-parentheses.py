class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(path,openN,closeN):
            if openN==closeN==n:
                res.append(path)
                return
            if openN<n:
                backtracking(path+'(',openN+1,closeN)
            if closeN<openN:
                backtracking(path+')',openN,closeN+1)
        backtracking('',0,0)
        return res