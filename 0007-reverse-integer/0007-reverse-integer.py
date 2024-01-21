class Solution:
    def reverse(self, x: int) -> int:
        res = str(x)[::-1]
        if res[-1].isalnum():
            res = int(res)
            if (-2)**31<=res<=((2**31)-1):
                return res
            else:
                return 0
        else:
            res=res[:-1]
            res=-int(res)
            if (-2)**31<=res<=((2**31)-1):
                return res
            else:
                return 0
            
        