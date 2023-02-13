class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans=(high-low)//2
        if high%2==1 or low%2==1:
            ans+=1
        return ans
