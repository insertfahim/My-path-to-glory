class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for item in nums:
            if item!=val:
                nums[i]=item
                i+=1
        return i
        