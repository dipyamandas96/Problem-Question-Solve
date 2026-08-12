class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        memo = {}

        def solve(i, j):
            if i >= m or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return abs(dungeon[i][j]) + 1 if dungeon[i][j] < 0 else 1
            if (i, j) in memo:
                return memo[(i, j)]

            down = solve(i + 1, j)
            right = solve(i, j + 1)

            needed = min(down, right) - dungeon[i][j]
            memo[(i, j)] = 1 if needed <= 0 else needed
            return memo[(i, j)]

        return solve(0, 0)