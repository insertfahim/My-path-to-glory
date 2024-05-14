class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)
        occurance_group = [ [] for i in range(len(nums)+1)]
        for item,times in freq_count.items():
            occurance_group[times].append(item)
        res=[]
        for items in occurance_group[::-1]:
            if items!=[] and k>0:
                res.extend(items)
                k-=len(items)
        return res