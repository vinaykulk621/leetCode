class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        ans,ans2,res="","",""
        if length>=10**4 or width>=10**4 or height>=10**4 or mass>=10**4 or length*width*height>=10**9:
            ans="Bulky"
        if mass>=100:
            ans2="Heavy"
        if ans=="Bulky" and ans2=="Heavy":
            res="Both"
        if ans!="Bulky" and ans2!="Heavy":
            res="Neither"
        if ans=="Bulky" and ans2!="Heavy":
            res=ans 
        if ans!="Bulky" and ans2=="Heavy":
            res=ans2
        return res
