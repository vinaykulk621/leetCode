class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        valid,ans=[],[]
        for word in words:
            if word[0] in ['a','e','i','o','u'] and word[-1] in ['a','e','i','o','u']:
                valid.append(1)
            else:
                valid.append(0)
        for i,j in queries:
            ans.append(sum(valid[i:j+1]))
        return ans
