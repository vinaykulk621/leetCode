class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            binary,cnt=[*bin(i)[2:]],0
            for i in binary:
                if i=='1':
                    cnt+=1
            ans.append(cnt)
        return ans
