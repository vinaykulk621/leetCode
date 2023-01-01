class Solution:
    def countDigits(self, num: int) -> int:
        cnt=0
        number=str(num)
        for i in number:
            if num%int(i)==0:
                cnt+=1
        return cnt
        
