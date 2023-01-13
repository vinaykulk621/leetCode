class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=math.inf
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                temp=target-nums[i]-nums[left]-nums[right]
                if temp==0:
                    return target
                if abs(temp)<abs(ans) or abs(temp)==abs(ans):
                    ans=temp
                if temp>0:
                    left+=1
                else:
                    right-=1
        return target-ans
