class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # iterate through, making a set of s1 and a set with s2. s2 subset changes
        r = len(s1)
        for l in range(len(s2)-len(s1)+1):
            print(s2[l:r])
            if sorted(s2[l:r]) == sorted(s1):
                return True
            r +=1
        return False