class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for item in strs:
            mapping = [0]*26
            for i in item:
                mapping[ord(i)-97]+=1
            anagrams[str(mapping)].append(item)
        return anagrams.values()