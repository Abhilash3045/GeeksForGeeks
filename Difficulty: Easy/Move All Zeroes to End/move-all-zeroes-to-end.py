class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	c=[];r=[]
    	for i in arr:
    	    if i==0:
    	        c.append(0)
    	    else:
    	        r.append(i)
    	arr[:]=r+c