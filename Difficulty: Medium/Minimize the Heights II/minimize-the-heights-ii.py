class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        n=len(arr)
        smol=arr[0]+k;larj=arr[n-1]-k
        diff=arr[n-1]-arr[0]
        for i in range(1,n):
            if arr[i]-k<0:
                continue
            mini=min(smol, arr[i]-k)
            maxi=max(larj, arr[i-1]+k)
            diff=min(diff, maxi-mini)
        return diff