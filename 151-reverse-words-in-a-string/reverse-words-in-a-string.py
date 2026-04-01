class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        r =' '.join(w[::-1])
        return r