class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums)-2):
            
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                target = -(sorted_nums[i])
                
                if target > (sorted_nums[k] + sorted_nums[j]):
                    j += 1

                elif target < (sorted_nums[k] +sorted_nums[j]):
                    k -= 1

                else:
                    triplet = sorted([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    if triplet not in output:
                        output.append(triplet)
                    j += 1
                    k -= 1


        return output
