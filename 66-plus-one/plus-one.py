class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = ''.join(map(str,digits))
        i = int(j)+1
        r = list(map(int,str(i)))
        return r