class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=sum(matrix,[])
        print(arr)
        low,high=0,len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]==target:
                return True
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return False
