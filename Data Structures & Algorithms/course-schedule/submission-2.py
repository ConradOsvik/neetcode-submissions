class Node:
    def __init__(self, val, edges = None):
        self.val = val
        self.edges = [] if not edges else edges

    def addEdge(self, node):
        if node not in self.edges:
            self.edges.append(node)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        safe = set()
        exploring = set()

        def dfs(node):
            if node in safe:
                return True

            if node in exploring:
                return False

            exploring.add(node)

            for edge in node.edges:
                if not dfs(edge):
                    return False

            exploring.remove(node)
            safe.add(node)

            return True

        courses = {}

        for [a, b] in prerequisites:
            if a not in courses:
                courses[a] = Node(a)
            if b not in courses:
                courses[b] = Node(b)

            courses[b].addEdge(courses[a])

        for key in courses:
            if not dfs(courses[key]):
                return False
            
        return True