class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        dic =  dict()
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
            
        for char in t:
            if char in dic:
                dic[char] -=1 
            
        for value in dic.values():
            if value > 0:
                return False
        return True

