class Solution:
	def twoSum(self, arr, target):
		# code here
		h={}
		for i in arr:
		    comp=target-i
		    if comp in h:
		        return True
		    h[i]=1
	    return False