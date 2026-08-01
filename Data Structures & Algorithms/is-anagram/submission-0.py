class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicS = defaultdict(int)

        for char in s:
            dicS[char] += 1
            
        for char in t:
            dicS[char] -= 1
        
        for count in dicS.values():
            if count != 0:
                return False
        return True 