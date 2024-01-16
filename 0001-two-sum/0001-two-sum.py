class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for idx in range(len(nums)):
            gap = target - nums[idx]
            if gap in prev_nums:
                return [prev_nums[gap],idx]
            else:
                prev_nums[nums[idx]]=idx
                