class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) 
        n = len(matrix[0])
        cols = n - 1
        rows = 0
        
        while (rows < len(matrix) and cols >= 0):
            current = matrix[rows][cols]
            if current == target:
                return True
            elif current > target:
                cols -= 1
            else:
                rows += 1
        return False