from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        state = [UNVISITED for i in range(numCourses)]
        result = []

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
            result.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result[::-1]
