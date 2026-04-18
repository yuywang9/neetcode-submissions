class Solution:
    def encode(self, strs: List[str]) -> str:
        unify = ""
        for word in strs:
            length = str(len(word))
            copy = length + "#" + word
            unify += copy
        return unify
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res