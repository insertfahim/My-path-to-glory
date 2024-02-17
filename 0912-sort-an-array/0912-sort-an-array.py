class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums)

    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        lesser, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                lesser.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        return self.quickSort(lesser) + equal + self.quickSort(greater)