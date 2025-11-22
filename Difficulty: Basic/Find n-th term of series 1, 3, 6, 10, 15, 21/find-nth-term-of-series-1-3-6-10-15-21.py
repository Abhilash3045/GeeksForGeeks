#User function Template for python3

class Solution:
    def findNthTerm(self, n):
        # code here 
        if n==1:
            return 1
        else:
            return ((n+1)*n)//2