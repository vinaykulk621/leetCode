class Solution:
    def partitionString(self, s: str) -> int:
        tmp,count,i=[],0,0
        s=[*s]
        while i<len(s):
            if s[i] in tmp:
                tmp=[]
                count+=1
                i-=1
            else:
                tmp.append(s[i])
            i+=1
        return count+1
