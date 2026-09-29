class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initial understanding integer k (meaning)
        # use a dictionary to keep track of how many occurences of each integer
        # iterate through with k, use max value, and then until k iterations
        
        # Determining occurences of each value
        occurences = {}
        for i in nums:
            occurences[i] = occurences.get(i,0) + 1
        
        # determining k most
        ret_list = []
        j = 0
        while j < k:
            key = max(occurences, key=occurences.get)
            ret_list.append(key)
            occurences.pop(key)
            j +=1
        return ret_list