class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max=0
        for ch in strs:
            if ch.isdigit():
                if int(ch)>max:
                    max=int(ch)
            elif len(ch)>max:
                max=len(ch)
        return max
