class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest=min(strs,key=len)
        for i,ch in enumerate(smallest):
            for otherword in strs: 
                if otherword[i]!=ch:
                    return smallest[:i]
        return smallest
