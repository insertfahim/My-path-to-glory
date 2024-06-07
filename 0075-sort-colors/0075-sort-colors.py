class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=[0,0,0]
        for object in nums:
            counter[object]+=1
        k=0
        for i in range(len(counter)):
            for j in range(counter[i]):
                nums[k]=i
                k+=1
        