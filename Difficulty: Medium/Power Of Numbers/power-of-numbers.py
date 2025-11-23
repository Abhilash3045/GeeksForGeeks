class Solution:
    def reverseexponentiation(self, n):
        # code here
        sn=str(n)
        rev=sn[::-1]
        return pow(n,int(rev))