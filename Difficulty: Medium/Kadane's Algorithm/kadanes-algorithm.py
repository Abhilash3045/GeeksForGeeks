class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        cs=0
        ms=float("-inf")
        for i in arr:
            cs+=i
            ms=max(ms,cs)
            if cs<0:
                cs=0
        return ms