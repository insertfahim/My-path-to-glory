class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numsSet=set(nums)
        for i in numsSet:
            if i-1 not in numsSet:
                count=1
                nextNum=i+1
                while nextNum in numsSet:
                    count+=1
                    nextNum+=1
                longest=max(count,longest)
        return longest