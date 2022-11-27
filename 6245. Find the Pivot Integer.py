class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        nums=[i for i in range(1,n+1)]
        left=nums[0]
        right=sum(nums)-left
        for i in range(2,n+1):
            left+=i
            if left==right:
                return i
            right-=i
        return -1
