class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return true if string s is a palindrome, else return false

        s = s.lower()
        clean = "".join(c for c in s if c.isalnum())

        back = len(clean) - 1
        
        for i in range(len(clean)):
            if clean[i] != clean[back]:
                return False
            back -= 1

        return True