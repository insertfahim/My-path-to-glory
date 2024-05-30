class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for item in nums:
            if item!=val:
                nums[l]=item
                l+=1
        return l
        