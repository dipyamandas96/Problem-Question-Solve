import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return bool(re.match(r"^[A-Z]+$|^[a-z]+$|^[A-Z][a-z]*$", word))