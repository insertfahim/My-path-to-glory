class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for number in str(num):
            if num%(int(number))==0:
                res+=1
        return res
        