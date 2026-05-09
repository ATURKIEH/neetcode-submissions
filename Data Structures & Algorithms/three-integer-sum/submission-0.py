class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        output  = []

        
        
        for i in range(len(sorted_array)-2):
            if i > 0  and sorted_array[i] == sorted_array[i-1]:
                continue
            j = i +1
            k = len(sorted_array) - 1

            while j<k:
                total = sorted_array[i] + sorted_array[j] + sorted_array[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1

                else:
                    output.append([sorted_array[i], sorted_array[j], sorted_array[k]])
                    while j < k and sorted_array[j] == sorted_array[j+1]:
                        j += 1
                    while j < k and sorted_array[k] == sorted_array[k-1]:
                        k -= 1
                    j += 1
                    k -= 1


        return output