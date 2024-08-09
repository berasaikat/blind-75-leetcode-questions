# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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
def find_node(root, val):
    if root is None or root.val == val:
        return root
    left_search = find_node(root.left, val)
    return left_search if left_search else find_node(root.right, val)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current_node = root
        while current_node:
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            else:
                return current_node
            
a = Solution()
root = build_tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
print(a.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 8)).val)
print(a.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 4)).val)