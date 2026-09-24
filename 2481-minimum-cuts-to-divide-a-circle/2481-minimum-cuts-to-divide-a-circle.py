class Solution:
    def numberOfCuts(self, n: int) -> int:
        return n//2 if not n%2 else (0 if n==1 else n)