 class Solution:
    def rob(self, nums: List[int]) -> int:
        copy=nums[:]
        if len(copy)==0:
            return 0
        elif len(copy)==1:
            return copy[-1]
        elif len(copy)==2:
            return max(copy[0],copy[-1])
        copy[1]=max(copy[0],copy[1])
        for i in range(2,len(nums)):
            copy[i] = max(copy[i-1], nums[i] + copy[i-2])
        return copy[-1]
