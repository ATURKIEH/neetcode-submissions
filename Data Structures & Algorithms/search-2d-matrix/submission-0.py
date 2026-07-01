class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        rows = len(matrix)
        columns = len(matrix[0])

        for row in range(0, rows):
            for column in range(0, columns):
                if matrix[row][column] == target:
                    found = True
                    return found
                else:
                    continue

        return found
