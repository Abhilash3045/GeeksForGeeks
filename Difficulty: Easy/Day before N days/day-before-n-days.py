class Solution:
    def findAnswer(self, d, n): 
       #Code here
        if d>n and n<7:
            return d-n
        if n>=7:
            return (7-(n%7))+d