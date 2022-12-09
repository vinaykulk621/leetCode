class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A=Counter(s)
        B=Counter(t)
        return set(s)==set(t) and len(s)==len(t) and A==B
