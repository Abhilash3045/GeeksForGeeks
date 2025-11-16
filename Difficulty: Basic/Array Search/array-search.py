class Solution:
    def search(self, arr, x):
        # code here
        return -1 if x not in arr else arr.index(x)