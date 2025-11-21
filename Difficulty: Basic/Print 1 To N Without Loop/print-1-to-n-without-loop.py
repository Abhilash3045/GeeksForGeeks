class Solution:    
    def printNos(self,n):
        #Code here
        def go(i):
            if i>n:
                return
            print(i,end=" ")
            go(i+1)
        go(1)
        