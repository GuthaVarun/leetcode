class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n1 =""
        s = 0
        for i in str(n):
            if i!="0":
                n1+=i

        if n1 == "":
            return 0
        for i in n1:
            s+=int(i)
        return int(n1)*s