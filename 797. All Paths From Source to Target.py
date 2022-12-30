class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(i, cur):
            if i==nodes-1:
                ans.append(cur[:])
                return
            for j in graph[i]:
                dfs(j,cur+[j])
        nodes,ans=len(graph),[]
        dfs(0,[0])
        return ans
