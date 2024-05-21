class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for item in range(n):
            res.append(nums[item])
            res.append(nums[item+n])
        return res