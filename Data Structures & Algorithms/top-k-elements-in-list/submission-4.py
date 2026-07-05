class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       seen = {}
       output = []

       for num in nums:
            if num in seen:
                seen[num] +=1
            else:
                seen[num] = 1

       for i in range(k):
            max_key = max(seen, key=seen.get)
            output.append(max_key)
            del seen[max_key]

       return output