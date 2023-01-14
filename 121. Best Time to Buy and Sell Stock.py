class Solution:
    def maxProfit(self,prices):
        left,right,ans=0,1,0
        while right<len(prices):
            temp=prices[right]-prices[left]
            if prices[left]<prices[right]:
                ans=max(temp,ans)
            else:
                left=right
            right+= 1
        return ans
