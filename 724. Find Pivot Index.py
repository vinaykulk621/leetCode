class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l,r=0,sum(nums)
        for i in range(len(nums)):
            if l==r-l-nums[i]:
                return i
            l+=nums[i]
        return -1
