class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res= []
        prefixes = []
        prefix = 1
        suffix = 1
        for num in nums:
            prefixes.append(prefix)
            prefix *=num
        for num in range(-1,(-len(nums))-1,-1):
            res.insert(0,prefixes[num]*suffix)
            suffix *= nums[num]
        return res