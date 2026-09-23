# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #9/23/26    
        # idea is to have a prev and a curr pointer

        prev = None
        curr = head

        #condition to continue until curr is none
        while curr:
            temp = curr.next    #store this because you're flipping the first two nodes
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev