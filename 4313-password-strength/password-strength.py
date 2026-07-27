class Solution:
    def passwordStrength(self, password: str) -> int:
        word = set(password)
        r=0
        for i in word:
            if i.islower():
                r+=1
            elif i.isupper():
                r+=2
            elif i.isdigit():
                r+=3
            else:
                r+=5
        return r