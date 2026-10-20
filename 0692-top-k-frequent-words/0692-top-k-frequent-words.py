class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        return [word for word, _ in nsmallest(k, Counter(words).items(), key=lambda x: (-x[1], x[0]))]