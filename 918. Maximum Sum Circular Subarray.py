# import math
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        maxVal=0
        max_so_far=nums[0]
        min_so_far=nums[0]
        minVal=0
        for i in range(len(nums)):
            total+=nums[i]
            maxVal=max(maxVal,0)+nums[i]
            max_so_far=max(max_so_far,maxVal)

            minVal=min(minVal,0)+nums[i]
            min_so_far=min(min_so_far,minVal)
        if min_so_far==total:
            return max_so_far
        return max(max_so_far,total-min_so_far)
