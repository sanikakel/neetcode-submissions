from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        state = [UNVISITED for i in range(numCourses)]

        for a,b in prerequisites:
            graph[b].append(a)
        
        def dfs(node):
            if state[node] == VISITING:
                return False
            if state[node] == VISITED:
                return True
            
            state[node] = VISITING
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
                        
            state[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
