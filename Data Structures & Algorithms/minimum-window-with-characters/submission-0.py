class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        freq_s = {}
        required = len(set(t))
        formed = 0

        l = 0
        result = (float('inf'),0,0)

        for letter in t:
            if letter not in freq_t:
                freq_t[letter] = 1
            else:
                freq_t[letter] +=1

        for r in range(len(s)):
            if s[r] not in freq_s:
                freq_s[s[r]] = 1
            else:
                freq_s[s[r]] +=1

            if freq_s[s[r]] == freq_t.get(s[r], 0):
                formed +=1
        
            while formed == required:
                if r - l + 1 < result[0]:
                    result = (r - l + 1, l, r)
                
                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    formed -=1

                l+=1

        return "" if result[0] == float('inf') else s[result[1]:result[2]+1]
