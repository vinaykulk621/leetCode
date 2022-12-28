class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        ans=[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0: 
                    ans[i][j]=j
                elif j == 0: 
                    ans[i][j] = i 
                elif word1[i-1]==word2[j-1]:
                    ans[i][j]=ans[i-1][j-1]
                else:
                    ans[i][j]=1+min(ans[i-1][j-1],ans[i][j-1],ans[i-1][j])
        print(ans)
        return ans[-1][-1]
