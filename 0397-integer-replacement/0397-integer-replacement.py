class Solution:
    def integerReplacement(self, n: int) -> int:
        def dp(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + dp(x // 2)
            return 1 + min(dp(x - 1), dp(x + 1))

        return dp(n)