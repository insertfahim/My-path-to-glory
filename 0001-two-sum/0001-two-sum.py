class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences={}
        for num in range(len(nums)):
            gap = target-nums[num]
            if gap in differences:
                return [differences[gap],num]
            differences[nums[num]]=num