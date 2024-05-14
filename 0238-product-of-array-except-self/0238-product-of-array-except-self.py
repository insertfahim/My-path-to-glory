class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res= []
        prefix = 1
        suffix = 1
        for num in nums:
            res.append(prefix)
            prefix *=num
        for num in range(-1,-len(nums)-1,-1):
            res[num]*=suffix
            suffix *= nums[num]
        return res