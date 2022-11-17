class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        try:
            ans1=nums.index(target)
        except:
            return [-1,-1]
        else:
            if not ans1 and ans1!=0:
                return [-1,-1]
            nums.reverse()
            ans2=nums.index(target)
            return [ans1,len(nums)-ans2-1]
