class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left,right,sumList=0,len(nums)-1,[]
        while left<right:
            sumList.append(nums[left]+nums[right])
            left+=1
            right-=1
        return max(sumList)
