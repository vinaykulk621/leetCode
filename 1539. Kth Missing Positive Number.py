class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt=0
        for i in range(1,10000):
            if i not in arr:
                cnt+=1
                if cnt==k:
                    break
        return i
