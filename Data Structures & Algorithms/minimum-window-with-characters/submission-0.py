class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        chars = {}
        for char in t:
            chars[char] = 1 + chars.get(char,0)
        # loop through, adjust freq map until it is same as t map or greater
            # Once it is the same, adjust left until less than then go back up
        l = 0
        r = 0
        s_map = {}
        match = 0
        while r < len(s):
            if s[r] in chars:
                s_map[s[r]] = 1 + s_map.get(s[r],0)
                if s_map[s[r]] == chars[s[r]]:
                    match += 1
            while match == len(chars):
                if len(ret) == 0:
                    ret = s[l:r+1]
                elif len(s[l:r+1]) < len(ret):
                    ret = s[l:r+1]
                if s[l] in chars:
                    s_map[s[l]] = s_map.get(s[l],0) - 1
                    if s_map[s[l]] < chars[s[l]]:
                        match -= 1
                l += 1
            r += 1
        return ret
            

                