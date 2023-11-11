class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        s=set(nums)
        for i in nums:
            if i-1 not in s:
                c=1
                j=i+1
                while j in s:
                    c+=1
                    j+=1
                longest=max(c,longest)
        return longest