class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0] *26
        freq2 = [0] *26

        for i in range (len(s)):
            freq1[ord(s[i]) - ord("a")] += 1

        for i in range (len(t)):
            freq2[ord(t[i]) - ord("a")] += 1
        
        return freq1 == freq2