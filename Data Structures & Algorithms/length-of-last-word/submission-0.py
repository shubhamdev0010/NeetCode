class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        isWordFound = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
                isWordFound = True
            elif isWordFound:
                break
        return length