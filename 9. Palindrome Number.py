class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x==int(str(x)[::-1])
