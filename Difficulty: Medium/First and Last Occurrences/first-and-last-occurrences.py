#User function Template for python3


class Solution:
    def find(self, arr, x):
        
        # code here
        minnu=float('inf');maxy=float('-inf')
        for i in range(len(arr)):
            if arr[i]==x:
                minnu=min(minnu,i)
                maxy=i
        return [minnu,maxy] if minnu!=float('inf') and maxy!=float('-inf') else [-1,-1]