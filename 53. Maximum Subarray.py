class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kabane's algo
        curMax,maxMax=0,-inf
        for num in nums:
            curMax=max(num,curMax+num)
            maxMax=max(maxMax,curMax)
        return maxMax
