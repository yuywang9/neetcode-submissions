class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoded = ""
        # for s in strs:
        #     encoded += f"{len(s)}:{s}"
        #     # We need to add : because what if the len number is multiple digits? How we identify the len with the numbers in the word? 
        # return encoded
        encoded = ""
        for i in strs:
            encoded += f"{len(i)}#{i}"
        return encoded





    def decode(self, s: str) -> List[str]:
        # res = []
        # i = 0
        # while i < len(s):
        #     j = i 
        #     while s[j] != ":":
        #         j += 1
        #     # now j is at #
        #     length = int(s[i : j])
        #     word = s[j + 1 : j + 1 + length]
        #     res.append(word)
        #     #update i
        #     i = j + 1 + length
        # return res
        res = []
        i = 0
        while i < len(s):
            j = i # j is for finding out the length number
            while s[j] != "#":
                j +=  1
            length = int(s[i : j])
            word = s[j + 1: j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res

























