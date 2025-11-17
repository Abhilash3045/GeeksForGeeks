class Solution:
    def medianOf2(self, a, b):
        # code here
        a+=b
        a.sort()
        if len(a)%2==0:
            return (a[len(a)//2]+a[len(a)//2-1])/2
        else:
            return a[len(a)//2]