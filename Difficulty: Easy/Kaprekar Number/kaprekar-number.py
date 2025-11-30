#User function Template for python3

class Solution:
    def isKaprekar(self,N):
        #code here
        temp=str(N*N)
        for i in range(1,len(temp)):
            left=int(temp[:i])
            right=int(temp[i:])
            if left==0 or right==0:
                continue
            if left+right==N:
                return 1
        return 0