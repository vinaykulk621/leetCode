class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans=Counter(nums)
        return list(filter(lambda x:ans[x]==1,ans))[0]
        
