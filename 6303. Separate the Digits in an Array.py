class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for i in range(len(nums)):
            for num in nums[i]:
                ans.append(int(num))
        return ans
