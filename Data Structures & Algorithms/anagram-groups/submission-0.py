class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initial idea: Iterate through list and sort all strings using a copy, add to map where key is sorted string and value is a list
        anagrams = {}
        anagrams_list = []
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(str)
            else:
                anagrams[sorted_str] = [str]

        for value in anagrams.values():
            anagrams_list.append(value)
        return anagrams_list
