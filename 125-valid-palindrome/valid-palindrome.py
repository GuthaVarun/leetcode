class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==' ':
            return True
        r = ''.join(i.lower() for i in s if i.isalnum())
        return True if r==r[::-1] else False