class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        s=[i for i in s]
        t=[i for i in t]
        for i in range(len(s)):
            if s[i]==t[0]:
                t.pop(0)
        return len(t)
