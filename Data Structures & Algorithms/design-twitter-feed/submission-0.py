import heapq
from typing import List
from collections import defaultdict

class Twitter:

    def __init__(self):
        # Global clock: increases every time a tweet is posted
        self.time = 0
        
        # Maps userId -> list of (time, tweetId)
        # Example: self.tweets[1] = [(1, 10), (3, 30)]
        self.tweets = defaultdict(list)
        
        # Maps userId -> set of followeeIds
        # Example: self.following[1] = {2, 3}
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        # Users to include: self + everyone I follow
        users = set(self.following[userId]) | {userId}
        
        # Put the latest tweet of each user into the heap
        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                # Use negative time to simulate a max-heap
                heapq.heappush(heap, (-time, tweetId, uid, idx))
        
        result = []
        while heap and len(result) < 10:
            neg_time, tweetId, uid, idx = heapq.heappop(heap)
            result.append(tweetId)
            
            # If this user has older tweets, push the next one
            if idx > 0:
                next_idx = idx - 1
                time, next_tweetId = self.tweets[uid][next_idx]
                heapq.heappush(heap, (-time, next_tweetId, uid, next_idx))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# ---------- TEST / DEMO ----------
if __name__ == "__main__":
    twitter = Twitter()
    
    twitter.postTweet(1, 10)
    twitter.postTweet(2, 20)
    print(twitter.getNewsFeed(1))   # [10]
    print(twitter.getNewsFeed(2))   # [20]
    
    twitter.follow(1, 2)
    print(twitter.getNewsFeed(1))   # [20, 10]
    print(twitter.getNewsFeed(2))   # [20]
    
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))   # [10]