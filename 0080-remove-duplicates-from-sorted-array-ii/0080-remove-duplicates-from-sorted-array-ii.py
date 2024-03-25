class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=2
        for j in range(2,len(nums)):
            if nums[j]!=nums[i-1]:
                nums[i]=nums[j]
                i+=1
            elif nums[i-1]==nums[j] and nums[i-2]==nums[j]:
                continue
            else:
                nums[i]=nums[j]
                i+=1
        return i