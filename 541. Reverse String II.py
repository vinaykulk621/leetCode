class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # convert the string to a list of characters
        s_list=list(s)
        n=len(s)
        i=0
        while i<n:
            # reverse the first k characters
            if i+k<=n:
                s_list[i:i+k]=s_list[i:i+k][::-1]
            # if fewer than k characters left, reverse all of them
            else:
                s_list[i:]=s_list[i:][::-1]
            # skip the next 2k characters
            i+=2*k
        return ''.join(s_list)
