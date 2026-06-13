class Node:
    def __init__(self, char):
        self.char = char
        self.adj = {}

class PrefixTree:
    def __init__(self):
        self.root = Node('.')

    def insert(self, word: str) -> None:
        i = 0
        n = len(word)
        curr = self.root
        while i < n and word[i] in curr.adj:
            curr = curr.adj[word[i]]
            i += 1
        while i < n:
            curr.adj[word[i]] = Node(word[i])
            curr = curr.adj[word[i]]
            i += 1
        curr.adj['.'] = ''

    def search(self, word: str) -> bool:
        i = 0
        n = len(word)
        curr = self.root
        while i < n and word[i] in curr.adj:
            curr = curr.adj[word[i]]
            i += 1
        return i == n and '.' in curr.adj

    def startsWith(self, prefix: str) -> bool:
        i = 0
        n = len(prefix)
        curr = self.root
        while i < n and prefix[i] in curr.adj:
            curr = curr.adj[prefix[i]]
            i += 1
        return i == n
        