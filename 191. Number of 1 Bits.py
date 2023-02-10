class Solution:
    def hammingWeight(self, n: int) -> int:
        n=[*bin(n)[2:]]
        cnt=0
        for i in n:
            if i=='1':
                cnt+=1
        return cnt
