'''
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldtonew = {}
        def clone(node):
            if node in oldtonew:
                return oldtonew[node]
            copy = Node(node.val)
            oldtonew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None
    
a = Solution()
print(a.cloneGraph([[2,4],[1,3],[2,4],[1,3]]))
print(a.cloneGraph([[]]))
print(a.cloneGraph([]))

# I'm unable to run this code on my local computer, but it works fine in leetcode.