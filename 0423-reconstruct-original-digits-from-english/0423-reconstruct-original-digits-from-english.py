class Solution:
    def originalDigits(self, s: str) -> str:

        words = [
            "zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"
        ]

        freq = Counter(s)

        owners = defaultdict(set)
        for i, word in enumerate(words):
            for ch in set(word):
                owners[ch].add(i)

        degree = {ch: len(ws) for ch, ws in owners.items()}
        q = deque(ch for ch in degree if degree[ch] == 1)

        result = []

        while q:
            ch = q.popleft()
            if degree[ch] != 1:
                continue

            digit = next(iter(owners[ch]))
            word = words[digit]

            count = freq[ch] // word.count(ch)
            result.extend([str(digit)] * count)

            for c in set(word):
                owners[c].remove(digit)
                degree[c] -= 1

                if degree[c] == 1:
                    q.append(c)

            for c in word:
                freq[c] -= count

        return "".join(sorted(result))


        