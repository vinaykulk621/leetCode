class Solution:
    def longestPalindrome(self, s: str) -> int:
        d,count={},0
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
            if d[ch]%2==1:
                count+=1
            else:
                count-=1
        if count>1:
            return len(s)-count+1
        return len(s)
