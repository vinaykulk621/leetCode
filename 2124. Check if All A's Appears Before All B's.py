class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a,b=0,0
        string=[item for item in s]
        for ch in string:
            if ch=='a':
                if b==1:
                    return False
                a=1
                continue
            elif ch=='b':
                b=1
                continue
        return True
