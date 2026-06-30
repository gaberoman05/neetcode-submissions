class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        chars = {}
        l = 0
        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r],0)
            while (r-l+1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l +=1
            length = max(length, r-l+1)
        return length