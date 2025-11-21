class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        res=0
        arr.sort()
        n=len(arr)
        for i in range(n-2):
            l=i+1;r=n-1
            while l<r:
                s=arr[i]+arr[l]+arr[r]
                if s<sum:
                    res+=(r-l)
                    l+=1
                else:
                    r-=1
        return res