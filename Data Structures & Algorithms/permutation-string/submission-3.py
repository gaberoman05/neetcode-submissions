class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        subset = {}
        for s in s1:
            subset[s] = 1 + subset.get(s,0)

        l = 0
        for r in range(len(s2)):
            print(s2[l:r])
            freq[s2[r]] = 1 + freq.get(s2[r],0)
            if len(s2[l:r]) >= len(s1): 
                freq[s2[l]] -= 1
                l += 1
            print(freq)
            if all(freq.get(k, 0) >= v for k, v in subset.items()):
                return True
        return False
