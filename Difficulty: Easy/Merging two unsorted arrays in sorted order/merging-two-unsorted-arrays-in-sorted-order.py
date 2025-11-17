class Solution:
    def sortedMerge(self, arr1,arr2,res):
        # Your code goes here
        m=arr1+arr2
        m.sort()
        for i in range(len(m)):
            res[i]=m[i]
        return res