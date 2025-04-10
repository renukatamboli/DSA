from heapq import heappush, heappop
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((-self.timestamp, tweetId)) 

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        ans = []
        follows = self.follows[userId]
        tweets = self.tweets[userId]
        for tweet in tweets:
            heappush(heap, tweet)
        for follow in follows:
            tweets = self.tweets[follow]
            for tweet in tweets:
                heappush(heap,tweet)
        i = 0
        while heap and i < 10:
            timestamp, tweetId = heappop(heap)
            ans.append(tweetId)
            i+=1
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
