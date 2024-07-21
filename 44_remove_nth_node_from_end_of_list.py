# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        right = head
        left = dummy

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


# Test cases
a = Solution()

head1 = create_linked_list([1, 2, 3, 4, 5])
result1 = a.removeNthFromEnd(head1, 2)
print_linked_list(result1)

head2 = create_linked_list([1])
result2 = a.removeNthFromEnd(head2, 1)
print_linked_list(result2)

head3 = create_linked_list([1, 2])
result3 = a.removeNthFromEnd(head3, 1)
print_linked_list(result3)