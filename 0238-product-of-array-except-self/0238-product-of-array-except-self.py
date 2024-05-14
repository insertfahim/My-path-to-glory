class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res= []
        prefixes = []
        suffixes = []
        prefix = 1
        suffix = 1
        for num in nums:
            prefixes.append(prefix)
            prefix *=num
        for num in nums[::-1]:
            suffixes.insert(0,suffix)
            suffix *=num
        for position in range(len(nums)):
            nums[position]=prefixes[position]*suffixes[position]
        return nums