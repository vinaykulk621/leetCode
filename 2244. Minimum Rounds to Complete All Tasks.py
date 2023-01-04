class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dummy,ans=Counter(tasks),0
        for val in dummy.values():
            if val==1:
                return -1
            if val%3==0:
                ans+=val//3
            else:
                ans+=val//3+1
        return ans
