class Solution:
    def divisorSubstrings(self, v: int, k: int) -> int:
        return sum(v%u==0 for u in map(int,findall(rf'(?=(.{{{k}}}))',str(v))) if u)