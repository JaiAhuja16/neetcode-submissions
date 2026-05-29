class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(wordList)
        adj = defaultdict(list)
        k = len(wordList[0])
        def match(word1, word2):
            f = 0
            for i in range(k):
                if word1[i] != word2[i]:
                    if f:
                        return False
                    f = 1
            return True

        for word in wordList:
            if match(beginWord, word):
                adj[beginWord].append(word)
        for word1 in wordList:
            for word2 in wordList:
                if match(word1, word2):
                    adj[word1].append(word2)
                    adj[word2].append(word1)
        q = deque([beginWord])
        visited = set(beginWord)
        c = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return c
                for word1 in adj[word]:
                    if word1 not in visited:
                        q.append(word1)
                        visited.add(word1)
            c += 1
        return 0
