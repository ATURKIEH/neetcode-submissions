class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        rows = len(matrix)
        columns = len(matrix[0])
        low = 0
        high = (rows * columns) - 1

        while low <= high:
            mid = (low+high)//2

            mid_element = matrix[mid//columns][mid%columns]

            if mid_element == target:
                found = True
                return found

            elif mid_element < target:
                low = mid + 1

            else:
                high = mid - 1

        return found



        
