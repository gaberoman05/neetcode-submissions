# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first need to find the size of the linked list
            # looping over and keeping track of size
            # to find n from end, just subtract size
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        # print(size)
        remove = size - n
        # print (remove)

        # Remove node n from end
            # have a tracker to keep postion
            # iterate until tracker is at position found in part 1
            # remove by changing previous pointer to current next
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        prev = dummy
        ind = 0
        while ind != remove + 1:
            prev = curr
            curr = curr.next
            ind += 1
        prev.next = curr.next
        return dummy.next


        