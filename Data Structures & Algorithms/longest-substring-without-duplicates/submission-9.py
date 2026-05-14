class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen     = set()
        best_len = 0
        l        = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best_len = max(best_len, r - l + 1)

        return best_len



        
        


        

            


        

        