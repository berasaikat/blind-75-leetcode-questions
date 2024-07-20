# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
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
        
a = Solution()
print(a.mergeTwoLists(ListNode([1,2,4]), ListNode([1,3,4])))
print(a.mergeTwoLists(ListNode([]), ListNode([])))
print(a.mergeTwoLists(ListNode([]), ListNode([0])))