class Solution:
    def countElements(self, matrix, target):
        n = len(matrix)
        count, row, col = 0, n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += (row + 1)
                col += 1
            else:
                row -= 1
        return count

    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[-1][-1]
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            count = self.countElements(matrix, mid)

            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans