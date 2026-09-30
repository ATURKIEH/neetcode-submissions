class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}


        for num in range(len(nums)):
            target_remainder = target - nums[num]
            if target_remainder in seen:
                return [seen[target_remainder], num]

            else:
                seen[nums[num]] = num

        


                

                




        