class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            prev = dp[0]
            for j in range(1, n + 1):
                prev2 = dp[j]
                if s[i] == s[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = prev2
        return dp[-1]