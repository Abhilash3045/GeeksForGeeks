class Solution:
    def findSum(self, n):
        # code here
        t=0
        for i in range(1,n+1):
            t+=i
        return t