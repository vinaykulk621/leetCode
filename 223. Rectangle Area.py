class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_of_A=(ay2-ay1)*(ax2-ax1)
        area_of_B=(by2-by1)*(bx2-bx1)

        x=min(ax2,bx2)-max(bx1,ax1)
        y=min(ay2,by2)-max(by1,ay1)

        xy=0
        
        if(x>0 and y>0):
            xy=x*y
            
        return area_of_A+area_of_B-xy
