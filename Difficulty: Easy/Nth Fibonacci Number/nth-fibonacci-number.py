class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n<=1:
            return n
        p2,p1=0,1
        for _ in range(1,n):
            c=p2+p1
            p2=p1
            p1=c
        return p1
        
