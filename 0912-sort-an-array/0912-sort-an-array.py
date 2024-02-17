class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right):
        if left >= right:
            return

        pivot = nums[random.randint(left, right)]
        i, j = left, right
        while i <= j:
            while i < right and nums[i] < pivot: # Find first i such that nums[i] >= pivot
                i += 1
            while j > left and nums[j] > pivot: # Find first j such that nums[j] <= pivot
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quickSort(nums, left, j) # nums[left..j] are elements < pivot
        self.quickSort(nums, i, right) # nums[i..right] are elements > pivot