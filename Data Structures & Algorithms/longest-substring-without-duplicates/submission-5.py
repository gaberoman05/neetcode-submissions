class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dynamic sliding window:
        # Begin at 0 and 1, keep a set of the window, and a max len, and running len
        l = 0
        if not s:
            return 0
        else:
            longest = 1
        while l < len(s)-1:
            r = l+1
            seen = {s[l]}
            while r<len(s) and s[r] not in seen:
                seen.add(s[r])
                r +=1
                print(str(l) + "," + str(r))
            if r-l > longest:
                longest = r-l
            l = l+1
        return longest