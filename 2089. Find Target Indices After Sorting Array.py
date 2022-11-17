class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1 and target==nums[0]:
            return [0]
        try:
            ans=nums.index(target)
        except:
            return []
        else:
            nums.sort()
            ans=nums.index(target)
            nums.reverse()
            ans_from_last=nums.index(target)
            res=len(nums)-ans-ans_from_last
            final=[]
            for i in range(res):
                final.append(ans+i)
            return final
