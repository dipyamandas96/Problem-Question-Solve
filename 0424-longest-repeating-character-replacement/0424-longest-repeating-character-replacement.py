class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        frequency = defaultdict(int)


        for right in range(len(s)):
            frequency[s[right]] += 1


            if right-left+1 - max(frequency.values()) <= k:
                max_len = max(max_len, right-left+1)
            else:
                frequency[s[left]] -= 1
                left += 1


        return max_len
