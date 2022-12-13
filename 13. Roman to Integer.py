class Solution:
    def romanToInt(self, s: str) -> int:
        ans,i=0,0
        while i<len(s)-1:
            if s[i]=='I' and s[i+1]=='V':
                i+=1
                ans+=4
            elif s[i]=='I' and s[i+1]=='X':
                i+=1
                ans+=9
            elif s[i]=='X' and s[i+1]=='L':
                i+=1
                ans+=40
            elif s[i]=='X' and s[i+1]=='C':
                i+=1
                ans+=90
            elif s[i]=='C' and s[i+1]=='D':
                i+=1
                ans+=400
            elif s[i]=='C' and s[i+1]=='M':
                i+=1
                ans+=900
            elif s[i]=='I':
                ans+=1
            elif s[i]=='V':
                ans+=5
            elif s[i]=='X':
                ans+=10
            elif s[i]=='L':
                ans+=50
            elif s[i]=='C':
                ans+=100
            elif s[i]=='D':
                ans+=500
            else:
                ans+=1000
            print(s[i],ans)
            i+=1
        if i==len(s):
            return ans
        if s[-1]=='I':
            ans+=1
        elif s[-1]=='V':
            ans+=5
        elif s[-1]=='X':
            ans+=10
        elif s[-1]=='L':
            ans+=50
        elif s[-1]=='C':
            ans+=100
        elif s[-1]=='D':
            ans+=500
        else:
            ans+=1000
        return ans
