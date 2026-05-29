class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(wordList)
        pat = defaultdict(list)
        k = len(wordList[0])
        for word in wordList:
            for i in range(k):
                pat[word[:i] + '*' + word[i + 1:]].append(word)

        q = deque([beginWord])
        visited = set(beginWord)
        c = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return c
                for i in range(k):
                    for j in pat[word[:i] + '*' + word[i + 1:]]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
            c += 1
        return 0
