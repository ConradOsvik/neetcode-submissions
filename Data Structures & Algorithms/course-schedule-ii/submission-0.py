class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for [a, b] in prerequisites:
            graph[b].append(a)

        safe = set()
        exploring = set()

        order = []
        
        def dfs(node):
            if node in safe:
                return True

            if node in exploring:
                return False

            exploring.add(node)

            for edge in graph[node]:
                if not dfs(edge):
                    return False

            exploring.remove(node)
            safe.add(node)
            order.append(node)

            return True

        for node in range(len(graph)):
            if not dfs(node):
                return []

        order.reverse()
        return order