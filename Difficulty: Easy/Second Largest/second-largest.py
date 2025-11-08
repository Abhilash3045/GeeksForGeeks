class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr=set(arr)
        arr=list(arr)
        arr.sort()
        if len(arr)>1:
            return arr[-2]
        return -1