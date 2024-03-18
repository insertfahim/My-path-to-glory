class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        place = [[] for i in range(len(nums)+1)]
        for item,freq in count.items():
            place[freq].append(item)
        res = []
        c = -1
        while c>=-(len(nums)) and k!=0:
            if place[c]!=[]:
                for item in place[c]:
                    if k>0:
                        res.append(item)
                        k-=1
                    else:
                        return res
                c-=1
            else:
                c-=1
        return res