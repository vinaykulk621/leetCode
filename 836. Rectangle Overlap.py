class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # overlap condition bro!!
        # min(left corordinates)-max(right cordinates)
        # for both the axes respective coordinates should be taken
        overlapX=min(rec1[2],rec2[2])-max(rec1[0],rec2[0])
        overlapY=min(rec1[3],rec2[3])-max(rec1[1],rec2[1])

        if overlapX>0 and overlapY>0:
            return True

        return False
