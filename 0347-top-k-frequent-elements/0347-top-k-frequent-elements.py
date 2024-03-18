class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        place = [[] for i in range(len(nums)+1)]
        for item,freq in count.items():
            place[freq].append(item)
        res = []
        for num in place[::-1]:
            for item in num:
                res.append(item)
                k-=1
                if k==0:
                    return res