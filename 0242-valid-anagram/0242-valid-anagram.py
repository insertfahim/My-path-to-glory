class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)
        for item in s:
            counter_s[item]+=1
        for item in t:
            counter_t[item]+=1
        return counter_s==counter_t