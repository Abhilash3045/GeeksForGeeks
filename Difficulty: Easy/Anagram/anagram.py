from collections import Counter
class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       return Counter(s1)==Counter(s2)