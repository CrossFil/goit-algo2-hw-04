from trie import Trie

class Homework(Trie):

    def __init__(self):
        super().__init__()
        self._words: list[str] = []

    def put(self, key: str, value):  # type: ignore[override]

        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        super().put(key, value)
        if key not in self._words:
            self._words.append(key)

    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise TypeError("pattern must be a string")
        if pattern == "":
            raise ValueError("pattern cannot be empty")

        return sum(1 for word in self._words if word.endswith(pattern))

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")
        if prefix == "":
            raise ValueError("prefix cannot be empty")

        return any(word.startswith(prefix) for word in self._words)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Suffix checks
    assert trie.count_words_with_suffix("e") == 1      # apple
    assert trie.count_words_with_suffix("ion") == 1    # application
    assert trie.count_words_with_suffix("a") == 1      # banana
    assert trie.count_words_with_suffix("at") == 1     # cat

    # Prefix checks
    assert trie.has_prefix("app") is True              # apple, application
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True              # banana
    assert trie.has_prefix("ca") is True               # cat

    print("All tests passed.")

# (base) admin@CrossFil-MBP ~ % python /Users/admin/PycharmProjects/Algo/hw_4_1.py
# All tests passed.