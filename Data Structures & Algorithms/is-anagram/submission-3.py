class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_t = {}
        seen_s = {}

        for letter in s:
            if letter in seen_s:
                seen_s[letter] += 1
            else:
                seen_s[letter] = 1

        for letter in t:
            if letter in seen_t:
                seen_t[letter] += 1
            else:
                seen_t[letter] = 1

        return seen_s == seen_t