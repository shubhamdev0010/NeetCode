class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # Agar left character alphanumeric nahi hai, toh usko skip karo
            if not s[l].isalnum():
                l += 1
                
            # Agar right character alphanumeric nahi hai, toh usko skip karo
            elif not s[r].isalnum():
                r -= 1
                
            # Jab dono valid characters mil jayein, toh unhe lowercase karke compare karo
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                
            # Agar match nahi karte, toh palindrome nahi hai
            else:
                return False
                
        return True