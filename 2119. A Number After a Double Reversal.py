class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True
        temp=num
        num=str(num)
        num=[*num]
        num.reverse()
        num=int("".join(num))
        num=str(num)
        num=[*num]
        num.reverse()
        num=int("".join(num))
        if temp==num:
            return True
        return False
