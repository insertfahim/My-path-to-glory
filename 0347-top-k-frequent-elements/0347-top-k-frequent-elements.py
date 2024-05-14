class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = Counter(nums)
        frequency_list = [[] for i in range(len(nums)+1)]
        for item,times in counting.items():
            frequency_list[times].append(item)
        res = []
        for i in frequency_list[::-1]:
            if i!=[]:
                res.extend(i)
                k-=len(i)
            if k==0:
                return res