class Solution:
    def sort012(self, arr):
        # code here
        z,o,t=0,0,0
        for i in arr:
            if i==0: z+=1
            elif i==1: o+=1
            else: t+=1
        i=0
        for _ in range(z):
            arr[i]=0; i+=1
        for _ in range(o):
            arr[i]=1; i+=1
        for _ in range(t):
            arr[i]=2; i+=1
        return arr