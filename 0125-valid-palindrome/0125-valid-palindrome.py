class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ''
        for char in s:
            if char.isalnum():
                phrase+=char.lower()
        return phrase==phrase[::-1]