class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums=[*set(nums)]
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    left+=1
        return ans
