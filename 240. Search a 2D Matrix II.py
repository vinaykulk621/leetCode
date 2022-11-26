class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans=sum(matrix,[])
        if target in ans:
            return True
        return False
