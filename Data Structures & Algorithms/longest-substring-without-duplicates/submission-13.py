class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = []
        best_len = 0
        for letter in s:
            string.append(letter)

        for i in range(len(string)):
            j = i
            seen = []
            while j < len(string):
                if string[j] in seen:
                    length = j - i
                    if length > best_len:
                        best_len = length
                    break

                    

                else:
                    seen.append(string[j])
                    j+=1
            else:
                length = j - i
                if length > best_len:
                    best_len = length 

        return best_len


        
                
            
        



        
        


        

            


        

        