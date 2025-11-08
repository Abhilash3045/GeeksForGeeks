class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        # left,right=0,len(arr)-1
        # while left<=right:
        #     mid=(left+right)//2
        #     if arr[mid]==k:
        #         return mid
        #     elif arr[mid]>k:
        #         right=mid-1
        #     else:
        #         left=mid+1
        # return -1
        for i in range(len(arr)):
            if arr[i]==k:
                return i
        return -1