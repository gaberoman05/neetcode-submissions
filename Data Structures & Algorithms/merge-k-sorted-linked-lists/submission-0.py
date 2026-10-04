# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1,l2))
            lists = merged_lists
        return lists[0]

    
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