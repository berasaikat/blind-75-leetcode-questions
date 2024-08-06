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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [root.val]
        def dfs(root):
            if not root:
                return 0
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            result[0] = max(result[0], root.val + left_max + right_max)
            return root.val + max(left_max, right_max)
        dfs(root)
        return result[0]

a = Solution()
print(a.maxPathSum(build_tree_from_list([1,2,3])))
print(a.maxPathSum(build_tree_from_list([-10,9,20,None,None,15,7])))