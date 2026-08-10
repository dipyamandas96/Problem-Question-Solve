class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def inBounds(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def dfs(x, y):
            if not inBounds(x,y) or board[x][y] != "O":
                return

            board[x][y] = "T"
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        m, n = len(board), len(board[0])
        for col in range(n):
            if board[0][col] == "O": dfs(0, col)
            if board[m-1][col] == "O": dfs(m-1, col)

        for row in range(m):
            if board[row][0] == "O": dfs(row, 0)
            if board[row][n-1] == "O": dfs(row, n-1)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"

        return