class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        count=list(count.items())
        count.sort(reverse=True,key=lambda x:x[1])
        res=[]
        for i in range(k):
            res.append(count[i][0])
        return res