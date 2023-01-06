class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        avg=[]
        while nums:
            temp=(nums.pop(0)+nums.pop(-1))/2
            if temp not in avg:
                avg.append(temp)
        return len(avg)
