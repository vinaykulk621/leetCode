class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        while matrix:
            ans+=matrix.pop(0) ## top
            ans+=[row.pop() for row in matrix] ## right
            if not matrix or not matrix[0]: break
            ans+=matrix.pop()[::-1] ## bottom
            ans+=[row.pop(0) for row in matrix][::-1] ## left
            if not matrix or not matrix[0]: break
        return ans
