# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #10/27/26
        #Thought it was easy but realized i don't know how to write this into code...
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next #moves the pointer to the next list1 node
            else:
                node.next = list2
                list2 = list2.next #moves the pointer to the next list2 node
            node = node.next #now that i set the current node, move to the next node in the lists

        if list1 is not None:
            node.next = list1
        elif list2 is not None:
            node.next = list2
        
        return dummy.next
             









        # My idea: simply compare node by node. SInce it's a linked list, time complexity is O(n)

        # p1 =  list1.val
        # p2 = list2.val
        # combined = []
        # end = false

        # while not end:
        #     p1_end = False
        #     p2_end = False

        #     if p1_end and p2_end:
        #         break
        #     if p1.next == None:
        #         p1_end = True
        #     if p2.next == None:
        #         p2_end = True
            
        #     if p1 < p2:
        #         p1_n = p1.next

       