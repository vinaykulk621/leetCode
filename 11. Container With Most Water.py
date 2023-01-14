class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,ans=0,len(height)-1,0
        while left<right:
            temp=(right-left)*min(height[left],height[right])
            ans=max(ans,temp)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
