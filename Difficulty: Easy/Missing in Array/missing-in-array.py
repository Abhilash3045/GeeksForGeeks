class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)+1
        curr=sum(arr)
        future=sum(range(1,n+1))
        return future-curr