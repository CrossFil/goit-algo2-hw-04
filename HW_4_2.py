from trie import Trie
from typing import List


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings: List[str]) -> str:  # type: ignore[override]

        if not isinstance(strings, list):
            raise TypeError("strings must be a list of str")
        if not strings:
            return ""

        for s in strings:
            if not isinstance(s, str):
                raise TypeError("all elements must be strings")

        prefix = strings[0]

        if len(strings) == 1:
            return prefix

        for word in strings[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix


if __name__ == "__main__":
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["flower", "flow", "flight"]) == "fl"

    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["interspecies", "interstellar", "interstate"]) == "inters"

    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["dog", "racecar", "car"]) == ""

    print("All tests passed.")

# (base) admin@CrossFil-MBP ~ % python /Users/admin/PycharmProjects/Algo/hw_4_2.py
# All tests passed.