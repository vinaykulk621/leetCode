class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m-->row
        # n-->column
        rowVal=[1]*n
        for i in range(0,m-1):
            newRowVal=[1]*n
            for j in range(n-2,-1,-1):
                newRowVal[j]=newRowVal[j+1]+rowVal[j]
            rowVal=newRowVal
        return rowVal[0]
