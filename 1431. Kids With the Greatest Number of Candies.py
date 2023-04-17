class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans,maxi=[],max(candies)
        for n in candies:
            if n+extraCandies>=maxi:
                ans.append(True)
                continue
            ans.append(False)
        return ans
