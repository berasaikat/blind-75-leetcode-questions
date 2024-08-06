# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
def build_tree_from_list(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    index = 1
    while queue and index < len(vals):
        node = queue.pop(0)
        if index < len(vals) and vals[index] is not None:
            node.left = TreeNode(vals[index])
            queue.append(node.left)
        index += 1
        if index < len(vals) and vals[index] is not None:
            node.right = TreeNode(vals[index])
            queue.append(node.right)
        index += 1
    return root
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        q = deque()
        q.append(root)
        while q:
            q_length = len(q)
            level = []
            for i in range(q_length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result

a = Solution()
print(a.levelOrder(build_tree_from_list([3,9,20,None,None,15,7])))
print(a.levelOrder(build_tree_from_list([1])))
print(a.levelOrder(build_tree_from_list([])))