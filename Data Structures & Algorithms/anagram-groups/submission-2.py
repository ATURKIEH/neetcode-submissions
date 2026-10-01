class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        output = []
        for word in strs:
            count = {}
            for letter in word:
                if letter in count:
                    count[letter]+=1
                else:
                    count[letter]=1

            count_key = tuple(sorted(count.items()))
            if count_key in groups.keys():
                groups[count_key].append(word)
            else:
                groups[count_key] = [word]

        for key, value in groups.items():
            output.append(value)
        return output

         


        