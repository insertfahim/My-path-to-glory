class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for number in range(len(nums)):
            if nums[number]>0:
                return triplets
            elif (number==0) or nums[number]!=nums[number-1]:
                first_num = nums[number]
                gap = 0 - first_num
                l,r = number+1, len(nums)-1
                while l<r:
                    if nums[l]+nums[r]==gap:
                        triplets.append([nums[number],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1
                    elif nums[l]+nums[r]<gap:
                        l+=1
                    elif nums[l]+nums[r]>gap:
                        r-=1
        return triplets