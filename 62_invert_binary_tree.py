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
def tree_to_list(root):
    """Helper function to convert a binary tree to a list using level-order traversal."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    return result

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        temp_var = root.left
        root.left = root.right
        root.right = temp_var

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
a = Solution()
print(tree_to_list(a.invertTree(build_tree_from_list([4,2,7,1,3,6,9]))))
print(tree_to_list(a.invertTree(build_tree_from_list([2,1,3]))))
print(tree_to_list(a.invertTree(build_tree_from_list([]))))