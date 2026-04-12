class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0 
        for z in range(isqrt(len(s))+1): 
            j = zeroj = 0 
            k = zerok = onek = 0 
            for i, ch in enumerate(s): 
                if ch == '0': zeroj += 1; zerok += 1
                else: onek += 1
                while zeroj > z: 
                    if s[j] == '0': zeroj -= 1
                    j += 1
                while zerok > z or k <= i and zerok == z and onek >= zerok**2: 
                    if s[k] == '0': zerok -= 1
                    else: onek -= 1
                    k += 1
                ans += k-j
        return ans 