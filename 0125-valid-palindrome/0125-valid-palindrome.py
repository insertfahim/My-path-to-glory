class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for item in s:
            if item.isalnum():
                new_string+=item.lower()
        l,r =0,len(new_string)-1
        while l<r:
            if new_string[l]!=new_string[r]:
                return False
            l+=1
            r-=1
        return True