from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentenceFrequency = defaultdict(int)

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.currentNode = self.root
        self.currentPrefix = ""
        self.sentenceFrequency = defaultdict(int)

        for i, sentence in enumerate(sentences):
            self._insert(sentence, times[i])

    def _insert(self, sentence, frequency):
        node = self.root
        self.sentenceFrequency[sentence] += frequency
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentenceFrequency[sentence] += frequency

    def input(self, c):
        if c == '#':
            self._insert(self.currentPrefix, 1)
            self.currentNode = self.root
            self.currentPrefix = ""
            return []

        self.currentPrefix += c
        if c in self.currentNode.children:
            self.currentNode = self.currentNode.children[c]
        else:
            self.currentNode.children[c] = TrieNode()
            self.currentNode = self.currentNode.children[c]

        matchedSentences = self.currentNode.sentenceFrequency
        sortedSentences = sorted(
            matchedSentences.keys(),
            key=lambda x: (-matchedSentences[x], x)
        )

        return sortedSentences[:3]