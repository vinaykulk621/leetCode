class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        vis,queue,ans=[],[],100001
        vis.append(n)
        queue.append(n)
        while queue:
            m=queue.pop(0)
            neighbours=[]
            for neighbour in roads:
                if neighbour[0]==m:
                    neighbours.append(neighbour[1])
                    if neighbour[2]<ans:
                        ans=neighbour[2]
                        continue
                if neighbour[1]==m:
                    neighbours.append(neighbour[0])
                    if neighbour[2]<ans:
                        ans=neighbour[2]
            for neighbour in neighbours:
                if neighbour not in vis:
                    vis.append(neighbour)
                    queue.append(neighbour)
        return ans
