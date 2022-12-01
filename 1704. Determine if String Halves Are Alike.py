class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        countA,countB,vow=0,0,['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)//2):
            if a[i] in vow:
                countA+=1
            if b[i] in vow:
                countB+=1
        return countA==countB
