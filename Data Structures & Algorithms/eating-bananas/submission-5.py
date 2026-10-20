
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = None
        while low <= high:
            mid = (low+high)//2
            sum = 0
            for i in piles:
                sum += math.ceil(i/mid)
            if sum <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid +1
                
        return ans
            



        

        