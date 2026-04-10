class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s :    
            d[i] = d.get(i,0)+1
        for i,j in enumerate(s):
            if d[j] == 1 :
                return i
                break
        return -1