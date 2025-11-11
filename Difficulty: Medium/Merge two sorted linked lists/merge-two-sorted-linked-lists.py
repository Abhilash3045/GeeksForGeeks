'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        h=[]
        curr=head1
        while curr:
            h.append(curr.data)
            curr=curr.next
        curr=head2
        while curr:
            h.append(curr.data)
            curr=curr.next
        dummy=Node(0)
        curr=dummy
        h.sort()
        for i in h:
            curr.next=Node(i)
            curr=curr.next
        return dummy.next
        