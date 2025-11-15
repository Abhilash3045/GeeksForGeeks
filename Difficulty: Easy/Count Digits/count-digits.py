#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        c=0
        l=[int(i) for i in str(n)]
        for i in l:
            if i!=0 and n%i==0:
                c+=1
        return c