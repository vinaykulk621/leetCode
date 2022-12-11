class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        neg,pos,ans,occur=0,0,[],0
        for ch in s:
            if ch==" ":
                if occur==1:
                    break
            elif ch=='-' and not pos and not occur:
                neg=1
                occur=1
            elif ch=='+' and not neg and not occur:
                pos=1
                occur=1
            elif ch.isdigit():
                ans.append(ch)
                occur=1
            elif not ch.isdigit():
                break
        if not ans:
            return 0
        ans=int("".join(map(str,ans)))
        if neg:
            ans=0-ans
            if ans<-2**31:
                return -2**31
        elif ans>2**31-1:
            return 2**31-1
        return ans
