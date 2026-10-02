class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        long = 1
        max_freq = 1
        freq = {}
        while r < len(s):
            freq[s[r]] = freq.get(s[r],0) + 1
            max_freq = max(max_freq, freq[s[r]])
            if (r-l+1)-max_freq > k:
                freq[s[l]] -= 1
                max_freq = max(max_freq, freq[s[l]])
                l +=1
            long = max(long, r-l+1)
            r += 1
        return long
