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
            for t, pid in self.posts[fid]:
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
