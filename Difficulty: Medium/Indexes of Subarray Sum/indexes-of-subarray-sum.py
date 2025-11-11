#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        curr=0
        i=0
        for j in range(len(arr)):
            curr+=arr[j]
            while curr>target and i<=j:
                curr-=arr[i]
                i+=1
            if curr==target:
                return (i+1,j+1)
        return [-1]