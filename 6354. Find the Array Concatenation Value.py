class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans=0
        start,end=0,len(nums)
        while nums:
            if len(nums)==1:
                ans+=nums[0]
                break
            tmp=int(str(nums.pop(0))+str(nums.pop(-1)))
            ans+=tmp
        return ans
