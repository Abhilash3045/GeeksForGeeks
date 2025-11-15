class Solution:
    def majorityElement(self, arr):
        #code here
        h={}
        for i in arr:
            h[i]=h.get(i,0)+1
        km=max(h, key=h.get)
        num=h[km]
        return km if num>len(arr)/2 else -1