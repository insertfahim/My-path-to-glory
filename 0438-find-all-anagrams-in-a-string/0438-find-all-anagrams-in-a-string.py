class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        counter_p = Counter(p)
        counter_s = defaultdict(int)
        for item in range(len(p)):
            counter_s[s[item]]+=1
        res = []
        l,r = 0,len(p)-1
        if counter_p==counter_s:
            res.append(l)
        for i in range(len(p),len(s)):
            if counter_s[s[l]]==1:
                counter_s.pop(s[l])
            else:
                counter_s[s[l]]-=1
            l+=1
            r+=1
            counter_s[s[r]]+=1
            if counter_s==counter_p:
                res.append(l)
        return res