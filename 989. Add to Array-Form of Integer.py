class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=[str(i) for i in num]
        n="".join(n)
        n=int(n)
        n=str(k+n)
        ans=[]
        for i in n:
            ans.append(int(i))
        return ans
