class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend/divisor>2**31-1:
            return 2**31-1
        if dividend/divisor<-2**31:
            return -2**31
        return int(dividend/divisor)
