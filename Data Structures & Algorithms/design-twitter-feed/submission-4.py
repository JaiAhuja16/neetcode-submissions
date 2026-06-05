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
            if self.posts[fid]:
                t, pid = self.posts[fid][-1]
                heapq.heappush(heap, (t, pid, len(self.posts[fid]) - 1, fid))
        l = 0
        while heap and l < 10:
            _, pid, ind, fid = heapq.heappop(heap)
            L.append(pid)
            ind -= 1
            l += 1
            if ind >= 0:
                t, pid = self.posts[fid][ind]
                heapq.heappush(heap, (t, pid, ind, fid))
        return L

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
