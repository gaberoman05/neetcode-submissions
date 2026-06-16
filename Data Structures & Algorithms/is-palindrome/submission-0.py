class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initial idea: using two point to iterate from front and back
        # other idea: reverse string and check for equality
        # Biggest blocker: dealing with non alphanumeric chars
        s_an = "".join(c for c in s if c.isalnum())
        return s_an.lower() == s_an[::-1].lower()