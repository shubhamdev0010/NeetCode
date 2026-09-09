class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        dic = dict()

        for char in arr:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        
        distinct_count = 0
        
        for char in arr:
            if dic[char] == 1:
                distinct_count += 1
                
                if distinct_count == k:
                    return char
        return ""