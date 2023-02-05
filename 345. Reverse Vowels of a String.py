class Solution:
    def reverseVowels(self, s: str) -> str:
        s=[*s]
        def vowel(ch):
            return ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or
             ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'
        start,end=0,len(s)-1
        while start<end:
            while start<len(s) and not vowel(s[start]):
                start+=1
            while end>=0 and not vowel(s[end]):
                end-=1
            if start<end:
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1
        return "".join(s)
