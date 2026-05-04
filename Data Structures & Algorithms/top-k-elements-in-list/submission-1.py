class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        output = []
        for n in range(len(nums)):
            if nums[n] in seen:
                seen[nums[n]] +=1
            else:
                seen[nums[n]] = 1
        
        for i in range(k):
            max_key = max(seen, key=seen.get)
            output.append(max_key)
            del seen[max_key]

        return output