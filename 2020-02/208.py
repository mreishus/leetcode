#!/usr/bin/env python

"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def get_or_add(self, char: str):  # -> TrieNode:
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]

    def get(self, char: str):  # -> Optional[TrieNode]:
        if char in self.children:
            return self.children[char]
        return None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pointer = self.root
        for char in word:
            pointer = pointer.get_or_add(char)
        pointer.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pointer = self.root
        for char in prefix:
            if pointer is None:
                return False
            pointer = pointer.get(char)
        return pointer and pointer.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.root
        for char in prefix:
            if pointer is None:
                return False
            pointer = pointer.get(char)
        return pointer


if __name__ == "__main__":
    t = Trie()
    words = ["Car", "Cat", "Done", "Try", "Trie", "Do"]
    for w in words:
        t.insert(w)
    for w in words:
        assert t.search(w) == True
    for w in ["Door", "ZZZ", "Ca", "---"]:
        assert t.search(w) == False
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
