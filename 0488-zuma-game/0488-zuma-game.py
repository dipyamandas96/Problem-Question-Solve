class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        memo = {}

        def collapse(s: str) -> str:
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[i] == s[j]:
                    j += 1
                if j - i >= 3:
                    return collapse(s[:i] + s[j:])
                i = j
            return s

        def is_good_place(s: str, pos: int, ball: str) -> bool:
            # Scenario 1: Extend an existing same-color run
            if pos > 0 and s[pos - 1] == ball:
                return True
            # Scenario 2: Split an identical pair to enable nested cascades
            if 0 < pos < len(s) and s[pos - 1] == s[pos]:
                return True
            return False

        def dfs(b: str, h: str) -> int:
            if not b:
                return 0
            if not h:
                return -1

            key = b + '#' + h
            if key in memo:
                return memo[key]

            min_steps = float('inf')

            for i in range(len(h)):
                # Prune duplicate balls in hand at the same recursion depth
                if i > 0 and h[i] == h[i - 1]:
                    continue

                ball = h[i]
                next_hand = h[:i] + h[i + 1:]

                for j in range(len(b) + 1):
                    if not is_good_place(b, j, ball):
                        continue

                    inserted = b[:j] + ball + b[j:]
                    collapsed = collapse(inserted)

                    sub_steps = dfs(collapsed, next_hand)
                    if sub_steps != -1:
                        min_steps = min(min_steps, sub_steps + 1)

            res = -1 if min_steps == float('inf') else min_steps
            memo[key] = res
            return res

        sorted_hand = "".join(sorted(hand))
        return dfs(board, sorted_hand)