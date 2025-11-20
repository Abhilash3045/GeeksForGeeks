class Solution:
    def maxWater(self, arr):
        # code here
        left=0;right=len(arr)-1
        lmax=0;rmax=0
        water=0
        while left<right:
            if arr[left]<arr[right]:
                if arr[left]>=lmax:
                    lmax=arr[left]
                else:
                    water+=lmax-arr[left]
                left+=1
            else:
                if arr[right]>=rmax:
                    rmax=arr[right]
                else:
                    water+=rmax-arr[right]
                right-=1
        return water