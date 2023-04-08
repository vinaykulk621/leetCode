class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[*s]
        s=[i.lower() for i in s if i.isalnum()]
        return "".join(s)=="".join(s)[::-1]
