# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. traverse and find the middle
        curr = head
        nodes = 0
        while curr:
            nodes += 1
            curr = curr.next
        middle = (nodes+1)//2
        #print(nodes)
        count = 0
        curr = head
        prev = None
        while count < middle:
            prev = curr
            curr = curr.next
            #print(curr.val)
            count +=1
        prev.next = None
        #2. reverse the second half
        prev_n = None
        while curr:
            next_n = curr.next
            curr.next = prev_n
            prev_n = curr
            curr = next_n
        #3. integrate the second half into the original
            # head is beginning, prev_n is the middle
        curr_o = head # original head
        curr_r = prev_n # reversed second half head
        while curr_o and curr_r:
            curr_o_next = curr_o.next # next in unaltered first half
            curr_r_next = curr_r.next # next in reversed 2nd half pre merge
            curr_o.next = curr_r
            curr_r.next = curr_o_next
            curr_r = curr_r_next
            curr_o = curr_o_next



    