# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedlist = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                list3 = self.mergeTwoLists(list1, list2)
                mergedlist.append(list3)
            lists = mergedlist
        return lists[0]

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        list3 = dummy

        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

        if list1:
            list3.next = list1
        elif list2:
            list3.next = list2

        return dummy.next

# Test cases
a = Solution()

lists1 = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]
result1 = a.mergeKLists(lists1)
print_linked_list(result1) 

lists2 = []
result2 = a.mergeKLists(lists2)
print_linked_list(result2)  

lists3 = [create_linked_list([])]
result3 = a.mergeKLists(lists3)
print_linked_list(result3) 