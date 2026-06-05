class Twitter:

    def __init__(self):
        self.all_posts = []
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.all_posts.append((userId, tweetId))
        self.posts[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        L = []
        c = 0
        for i, (uid, pid) in enumerate(self.all_posts[::-1]):
            if c == 10:
                break
            if uid in self.follows[userId] or uid == userId:
                L.append(pid)
                c += 1 
        return L

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
