"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(node):
            if not node:
                return

            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
                else:
                    if visited[neighbor] not in clone.neighbors:
                        clone.neighbors.append(visited[neighbor])
                    if clone not in visited[neighbor].neighbors:
                        visited[neighbor].neighbors.append(clone)

        dfs(node)

        return visited[node]
