class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums=set(nums)
        for num in nums:
            rail = [num]
            add=1
            if num-1 not in nums:
                while True:
                    if num+add in nums:
                        rail.append(num+add)
                        add+=1
                    else:
                        break
            res = max(res,len(rail))
        return res