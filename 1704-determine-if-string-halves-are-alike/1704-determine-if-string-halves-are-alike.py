class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2
        b = s[0:mid]
        c = s[mid:]
        vowels = ['a','e','i','o','u']
        b_count = {'v':0,
                  'c': 0}
        c_count = {'v':0,
                  'c': 0}
        for i in range(mid):
            if b[i].lower() in vowels:
                b_count['v']+=1
            else:
                b_count['c']+=1
            if c[i].lower() in vowels:
                c_count['v']+=1
            else:
                c_count['c']+=1
        return b_count==c_count