# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower,higher=0,n
        while lower<higher:
            mid=lower+(higher-lower)//2
            if not isBadVersion(mid):
                lower=mid+1
            else:
                higher=mid
        return lower
