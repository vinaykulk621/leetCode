class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        total=Counter(arr)
        unique=set(total.values())
        return len(unique)==len(total.values())
