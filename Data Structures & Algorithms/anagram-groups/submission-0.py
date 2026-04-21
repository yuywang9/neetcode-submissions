class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for string in strs:
            key = [0] * 26
            for s in string:
                key[ord(s) - ord("a")] += 1
            if tuple(key) in freq:
                freq[tuple(key)].append(string)
            else:
                freq[tuple(key)] = [string]

        res = []
        for val in freq.values():
            res.append(val)
        
        return res