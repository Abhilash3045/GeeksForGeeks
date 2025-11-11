"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        h=[]
        curr=head
        while curr:
            h.append(curr.data)
            curr=curr.next
        h.reverse()
        dummy=Node(0)
        curr=dummy
        for i in h:
            curr.next=Node(i)
            curr=curr.next
        return dummy.next
        