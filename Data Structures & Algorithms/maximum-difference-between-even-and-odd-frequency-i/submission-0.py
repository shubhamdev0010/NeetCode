class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}

        # Count frequency of each character
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        max_odd = 0
        min_even = float('inf')

        # Find maximum odd and minimum even frequency
        for value in dic.values():
            if value % 2 == 1:
                max_odd = max(max_odd, value)
            else:
                min_even = min(min_even, value)

        return max_odd - min_even