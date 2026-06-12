class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        for i in range(len(nums)):
            if nums[i] == target:
                found = True
                return i
        if found == False:
            return -1
        