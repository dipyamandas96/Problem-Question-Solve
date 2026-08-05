class Solution:
    def numberOfSpecialChars(self, s: str) -> int:
        return sum(0<=s.rfind(c)<s.find(c.upper()) for c in ascii_lowercase)