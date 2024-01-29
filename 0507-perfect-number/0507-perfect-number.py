class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        if num==1:
            return False
        for number in range(1,int(num**0.5)+1):
            if num%number==0:
                res+=number
                res+=num//number
        res-=num
        return res==num
        