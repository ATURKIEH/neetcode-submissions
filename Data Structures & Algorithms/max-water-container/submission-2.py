class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0 
        i = 0
        j = len(heights) - 1

        while i<j:
            volume = min(heights[i], heights[j]) * (j-i)
            if volume < best:
                if heights[i] < heights[j]:
                    i+=1
                else:
                    j-=1
            else:
                best = volume
                if heights[i] < heights[j]:
                    i+=1
                else:
                    j-=1
        return best

