# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.next = None
        if isinstance(x, list):
            self.val = x[0]
            current = self
            self.nodes = [self]
            for value in x[1:]:
                new_node = ListNode(value)
                current.next = new_node
                current = new_node
                self.nodes.append(current)
        else:
            self.val = x

    def create_cycle(self, pos):
        if pos != -1:
            cycle_entry = self.nodes[pos]
            current = self
            while current.next:
                current = current.next
            current.next = cycle_entry
        return self

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


a = Solution()
print(a.hasCycle(ListNode([3, 2, 0, -4]).create_cycle(1)))  
print(a.hasCycle(ListNode([1, 2]).create_cycle(0)))        
print(a.hasCycle(ListNode([1]).create_cycle(-1))) 