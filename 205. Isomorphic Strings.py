class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        A,B=set(s),set(t)
        return len(A)==len(B) and len({(a,b) for a,b in zip(s,t)})==len(set(s))
