class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red=nums.count(0)
        white=nums.count(1)
        blue=nums.count(2)
        for i in range(len(nums)):
            if red:
                nums[i]=0
                red-=1
            elif white:
                nums[i]=1
                white-=1
            else:
                nums[i]=2
                blue-=1
