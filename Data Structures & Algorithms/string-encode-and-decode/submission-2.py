class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            string += str(len(strs[i])) + "|"+ strs[i]
        return string

    # not entirely sure how to account for situation where str length is variable from 1-3 digits
    def decode(self, s: str) -> List[str]:
        ret_list = []
        i = 0
        while i < len(s):
            d = i
            while s[d] != "|":
                d += 1
            s_len = int(s[i:d])
            ret_list.append(s[d+1:d+1+s_len])
            i = d+1+s_len
        return ret_list
        
    

