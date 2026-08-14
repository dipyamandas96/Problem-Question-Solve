class TrieNode:
    def __init__(self) -> None:
        self.dictionary = {}
        self.endOfTheWord = False


class WordDictionary:
    def __init__(self) -> None:
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.node
        for ch in word:
            curr.dictionary.setdefault(ch, TrieNode())
            curr = curr.dictionary[ch]
        curr.endOfTheWord = True

    def search(self, word: str) -> bool:
        return self.helper_search(self.node, list(word))

    def helper_search(self, node: TrieNode, word: list[str]) -> bool:
        if len(word) == 0:
            return bool(node.endOfTheWord)

        if not node.dictionary:
            return False

        if word[0] == ".":
            return any(
                self.helper_search(node.dictionary[ch], word[1:])
                for ch in node.dictionary
            )
        elif word[0] not in node.dictionary:
            return False

        return self.helper_search(node.dictionary[word[0]], word[1:])