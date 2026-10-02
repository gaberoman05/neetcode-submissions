# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2
        dummy = ListNode(0)
        curr = dummy
        while curr_1 or curr_2:
            if not curr_1:
                curr.next = curr_2
                break
            elif not curr_2:
                curr.next = curr_1
                break
            else:
                if curr_1.val <= curr_2.val:
                    curr.next = curr_1
                    curr_1 = curr_1.next
                else:
                    curr.next = curr_2
                    curr_2 = curr_2.next
            curr = curr.next
        return dummy.next
        