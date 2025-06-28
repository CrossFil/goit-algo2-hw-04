### Task 1 — Extending Trie Functionality

Implement two additional methods for a `Trie` class by creating a subclass `Homework`:

* `count_words_with_suffix(pattern)` — returns the number of words that end with the given suffix.
* `has_prefix(prefix)` — checks whether there exists any word that starts with the given prefix.

#### Technical Requirements

* Class `Homework` must inherit from a base class `Trie`.
* Both methods must validate input: arguments must be strings.
* `count_words_with_suffix` returns an integer.
* `has_prefix` returns a boolean.
* Basic error handling must be implemented for invalid inputs (e.g. empty strings or wrong types).

Test cases should verify the correct behavior of both methods on a small sample of inserted words.

---
### Task 2 — Finding the Longest Common Prefix

Implement a class `LongestCommonWord` that inherits from `Trie` and provides a method `find_longest_common_word(strings)` to find the longest prefix shared among all strings in the input list.

#### Technical Requirements

* The `LongestCommonWord` class must extend the `Trie` base class.
* The method `find_longest_common_word` takes a list of strings as input.
* The method returns a string representing the longest common prefix.
* Time complexity must be O(S), where S is the total length of all input strings.
* Input validation must be implemented:

  * Return an empty string for an empty list or if there is no common prefix.
  * Raise appropriate exceptions for invalid inputs (e.g., non-string elements).
