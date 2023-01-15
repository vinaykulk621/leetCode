class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        louda=0
        x=sum(nums)
        for num in nums:
            ch=str(num)
            for number in ch:
                numb=int(number)
                louda+=numb
        return abs(x-louda)
