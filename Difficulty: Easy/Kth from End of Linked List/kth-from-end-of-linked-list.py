'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        h=[]
        curr=head
        while curr:
            h.append(curr.data)
            curr=curr.next
        return h[-k] if len(h)>=k else -1