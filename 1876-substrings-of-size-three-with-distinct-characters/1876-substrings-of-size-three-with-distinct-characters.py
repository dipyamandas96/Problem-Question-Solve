class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(len({*t})==3 for t in findall(r'(?=(...))',s))