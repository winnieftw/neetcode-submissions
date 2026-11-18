# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #11/18/26

        '''
            0 ------> 0 ------> 0 ----> 0

        '''

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev #flip the next to point to prev
            prev = curr #prev should now be the current node
            curr = temp #move on to the next node

        return prev