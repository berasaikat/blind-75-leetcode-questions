# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        n = 0
        stack = []
        current_node = root
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            n += 1
            if n == k:
                return current_node.val
            current_node = current_node.right

a = Solution()
print(a.kthSmallest(build_tree_from_list([3,1,4,None,2]), 1))
print(a.kthSmallest(build_tree_from_list([5,3,6,2,4,None,None,1]), 3))