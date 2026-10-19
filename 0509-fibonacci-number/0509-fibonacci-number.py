class Solution:
    def solve(self, n: int, fibN: list) -> int:       
        if fibN[n] != -1:
            return fibN[n]
        fibN[n] = self.solve(n - 1, fibN) + self.solve(n - 2, fibN)
        return fibN[n]

    def fib(self, n: int) -> int:
        fibN = [-1] * 31
        fibN[0] = 0
        fibN[1] = 1
        return self.solve(n, fibN)
        