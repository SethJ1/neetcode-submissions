# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy = ListNode()
        tail = dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                tail.next = ListNode(cur2.val)
                cur2 = cur2.next
            tail = tail.next

        while cur1:
            tail.next = ListNode(cur1.val)
            tail = tail.next
            cur1 = cur1.next

        while cur2:
            tail.next = ListNode(cur2.val)
            tail = tail.next
            cur2 = cur2.next

        return dummy.next