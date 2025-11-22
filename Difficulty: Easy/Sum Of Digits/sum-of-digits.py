class Solution:
    def sumOfDigits(self, n):
        # code here
        s=0
        while n:
            d=n%10
            s+=d
            n//=10
        return s