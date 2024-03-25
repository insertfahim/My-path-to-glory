class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for char in s:
            if char.isalnum():
                t+=char.lower()
        i,j=0,len(t)-1
        while i<j:
            if t[i]!=t[j]:
                return False
            i+=1
            j-=1
        return True