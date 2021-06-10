"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        register = {node: Node(node.val)} #new Graph
        line = [node]
        while line:
            n = line.pop()
            for neigh in n.neighbors:
                if neigh not in register:
                    line.append(neigh)
                    register[neigh] = Node(neigh.val)
                
                register[n].neighbors.append(register[neigh])
        return register[node]
