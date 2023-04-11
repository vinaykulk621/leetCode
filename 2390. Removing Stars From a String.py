class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        s=[*s]
        for i in s:
            if i=='*':
                ans.pop(-1)
            else:
                ans.append(i)
        return "".join(ans)
