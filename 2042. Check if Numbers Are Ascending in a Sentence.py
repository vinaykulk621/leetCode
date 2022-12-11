class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp=-10000
        s=s.split()
        for ch in s:
            if ch==" ":
                continue
            if ch.isdigit():
                if temp<int(ch):
                    temp=int(ch)
                else:
                    return False
        return True
