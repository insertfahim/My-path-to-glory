class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a,b=min(nums),max(nums)
        while a>0 and b>0:
            if a>b:
                a=a%b
            else:
                b=b%a
        if a==0:
            return b
        return a
        