class Twitter:

    def __init__(self):
        self.c = 0
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.c, tweetId))
        self.c -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        L = []
        heap = []
        self.follows[userId].add(userId)
        for fid in self.follows[userId]:
            l = len(self.posts[fid])
            for j in range(l - 1, max(-1, l - 11), -1):
                t, pid = self.posts[fid][j]
                heapq.heappush(heap, (t, pid))
        l = 0
        while heap and l < 10:
            _, pid = heapq.heappop(heap)
            L.append(pid)
            l += 1
        return L

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
