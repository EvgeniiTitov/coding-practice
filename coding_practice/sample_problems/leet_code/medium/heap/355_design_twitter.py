from typing import List, MutableMapping, Set, Iterator
import heapq


"""
Summary: OOP, separation of concerns. Users could be treated as nodes in a graph.
Each node keep track of the nodes it connects to (followers -> followees). Use
heap to keep track of the most recent tweets for each user. 
_______________________________________________________________________________

https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user, and is able to see the 10 most recent tweets in 
the user's news feed.

Implement the Twitter class:

- Twitter() Initializes your twitter object.

- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId 
  by the user userId. Each call to this function will be made with a 
  unique tweetId.

- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet 
  IDs in the user's news feed. Each item in the news feed must be posted by 
  users who the user followed or by the user themselves. Tweets must be ordered 
  from most recent to least recent.

- void follow(int followerId, int followeeId) The user with ID followerId 
  started following the user with ID followeeId.

- void unfollow(int followerId, int followeeId) The user with ID followerId 
  started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

Thoughts:

Users
Tweets

Following User -> User
"""

# --------------------------------- MY TRY 1 ----------------------------------

def get_next_tweet_id() -> Iterator[int]:
    counter = 0
    while True:
        yield counter
        counter += 1


class Tweet:
    next_timestamp = get_next_tweet_id()

    def __init__(self, tweet_id: int) -> None:
        self.id = tweet_id
        self.timestamp = next(Tweet.next_timestamp)

    def __lt__(self, other: "Tweet") -> bool:
        return -self.timestamp < -other.timestamp

    def __repr__(self) -> str:
        return f"Tweet. Id: {self.id}; Timestamp: {self.timestamp}"


class User:
    """
    Every user has a news feed. Items in the news feed are either posted by
    the user themselves OR by the people they follow. The feed must be ordered
    by the post date, recent first.
    """
    def __init__(self, user_id: int) -> None:
        self.id = user_id
        self._following: Set["User"] = set()
        self._tweets: List[Tweet] = []
        heapq.heapify(self._tweets)

    def follow(self, user: "User") -> None:
        if user not in self._following:
            self._following.add(user)

    def unfollow(self, user: "User") -> None:
        if user in self._following:
            self._following.remove(user)

    def tweet(self, tweet_id: int) -> None:
        tweet = Tweet(tweet_id)
        heapq.heappush(self._tweets, tweet)

    def get_user_feed(self, nb_tweets: int) -> List[int]:
        """
        Return 10 tweets done either by user or its followers sorted by the
        most recent ones
        """
        # TODO: This could be optimised. Not quite there yet.
        #       1. Looping over friends O(k)
        #       2. Heapifying is unnecessary if no connections

        news_feed_pool = []

        # Get user tweets
        user_latest = heapq.nsmallest(nb_tweets, self._tweets)
        news_feed_pool.extend(user_latest)

        # Get followees tweets
        for followee_user in self._following:
            news_feed_pool.extend(followee_user.get_user_tweets(nb_tweets))

        heapq.heapify(news_feed_pool)
        return [
            tweet.id for tweet in
            heapq.nsmallest(10, news_feed_pool)
        ]

    def get_user_tweets(self, tweets_nb: int) -> List[Tweet]:
        return heapq.nsmallest(tweets_nb, self._tweets)

    def __str__(self) -> str:
        return (
            f"User. Id: {self.id}; Follows: {self._following}; "
            f"Tweets: {self._tweets}"
        )


class Twitter:

    def __init__(self):
        self._users: MutableMapping[int, User] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Composes a new tweet with ID tweetId by the user userId. Each call to
        this function will be made with a unique tweetId.
        """
        if userId not in self._users:
            user = User(userId)
            self._users[userId] = user
        else:
            user = self._users.get(userId)
        user.tweet(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed.
        Tweets must be ordered from most recent to least recent.
        """
        if userId not in self._users:
            return []
        user = self._users.get(userId)
        return user.get_user_feed(10)

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId follows the user with ID followeeId.
        """
        if followerId not in self._users:
            follower = User(followerId)
            self._users[followerId] = follower
        else:
            follower = self._users.get(followerId)

        if followeeId not in self._users:
            followee = User(followeeId)
            self._users[followeeId] = followee
        else:
            followee = self._users.get(followeeId)

        follower.follow(followee)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId unfollowed the user with ID followeeId
        """
        follower = self._users.get(followerId)
        followee = self._users.get(followeeId)
        follower.unfollow(followee)


def main():
    twitter = Twitter()

    twitter.postTweet(1, 5)
    twitter.postTweet(2, 3)
    twitter.postTweet(1, 101)
    twitter.postTweet(2, 13)
    twitter.postTweet(2, 10)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 94)
    twitter.postTweet(2, 505)
    twitter.postTweet(1, 333)
    twitter.postTweet(2, 22)
    twitter.postTweet(1, 11)
    twitter.postTweet(1, 205)
    twitter.postTweet(2, 203)
    twitter.postTweet(1, 201)
    twitter.postTweet(2, 213)
    twitter.postTweet(1, 200)
    twitter.postTweet(2, 202)
    twitter.postTweet(1, 204)
    twitter.postTweet(2, 208)
    twitter.postTweet(2, 233)
    twitter.postTweet(1, 222)
    twitter.postTweet(2, 211)

    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))


if __name__ == '__main__':
    main()
