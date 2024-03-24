class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums=set(nums)
        for num in nums:
            length=1
            if num-1 not in nums:
                while num+length in nums:
                    length+=1
            res = max(res,length)
        return res