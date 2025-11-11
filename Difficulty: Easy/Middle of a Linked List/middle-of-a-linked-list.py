'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        h=[]
        curr=head
        while curr:
            h.append(curr.data)
            curr=curr.next
        return h[len(h)//2]
        
