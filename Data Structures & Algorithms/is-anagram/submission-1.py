class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Pseudo Code
        Create hash maps for each string where char is key and val is # of occurences
        Iterate through each map and see if val for each char is the same
        """
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] +=1
            else:
                s_dict[s[i]] = 1
                
        for i in range(len(t)):
            if t[i] in t_dict:
                t_dict[t[i]] +=1
            else:
                t_dict[t[i]] = 1
        return s_dict == t_dict
        