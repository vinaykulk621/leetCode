class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
       first=Counter(word1)
       second=Counter(word2)
       A=set(word1)
       B=set(word2)
       C=sorted(first.values())
       D=sorted(second.values())
       return C==D and A==B
