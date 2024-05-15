class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        sequences = {}
        nums=set(nums)
        for num in nums:
            if (num-1 not in nums):
                sequences[num]=1
                next_num = num+1
                while next_num in nums:
                    sequences[num]+=1
                    next_num+=1
        return max(sequences.values())