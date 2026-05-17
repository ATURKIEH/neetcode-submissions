class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = []
        for letter in s:
            string.append(letter)

        best_len = 0
        l = 0
        r = 0
        seen = set()
        while r < len(string):
            if string[r] not in seen:
                seen.add(string[r])
                r += 1

            else:
                while string[r] in seen:
                    seen.remove(string[l])

                    l +=1

            length = r - l
            if length > best_len:
                best_len = length

        return best_len

                
            
        



        
        


        

            


        

        