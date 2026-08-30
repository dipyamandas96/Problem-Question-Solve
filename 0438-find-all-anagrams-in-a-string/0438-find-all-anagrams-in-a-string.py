class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n, m = len(p), len(s)
        res = []

        if n > m:
            return res

        # Frequency array for p
        p_c = [0] * 26
        for ch in p:
            p_c[ord(ch) - ord('a')] += 1

        # Frequency array for first window of s
        s_c = [0] * 26
        for st in s[:n]:
            s_c[ord(st) - ord('a')] += 1

        if s_c == p_c:
            res.append(0)                              # First window is an anagram

        # Slide window across s
        for i in range(n, m):
            s_c[ord(s[i]) - ord('a')] += 1            # Add incoming character
            s_c[ord(s[i - n]) - ord('a')] -= 1        # Remove outgoing character

            if s_c == p_c:
                res.append(i - n + 1)                  # Start index of current window

        return res