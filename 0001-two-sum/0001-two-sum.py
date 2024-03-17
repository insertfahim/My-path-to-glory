class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        place_holder = {}
        for index,value in enumerate(nums):
            gap = target-value
            if gap in place_holder:
                return [place_holder[gap],index]
            else:
                place_holder[value]=index
        