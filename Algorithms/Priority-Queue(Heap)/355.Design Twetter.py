from collections import defaultdict
import heapq
class Solution:
    def __init__(self):
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)
        self.time=0

    def postTweet(self,userId:int,tweetId:int)->None:
        self.time+=1
        self.tweetMap[userId].append((self.time,tweetId))

    def get_news_feed(self,userId:int):
        heap = []
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                index = len(self.tweetMap[user])-1
                time,tweet=self.tweetMap[user][index]
                heapq.heappush(heap,(-time,tweet,user,index))
        ans = []
        while heap and len(ans)<10:
            negTime,tweet,user,index=heapq.heappop(heap)
            ans.append(tweet)

            if index>0:
                index-=1
                time,tweet=self.tweetMap[user][index]
                heapq.heappush(heap,(-time,tweet,user,index))
        return ans  

    def follow(self,followerId:int,followeeId:int)->None:
        self.followMap[followerId].add(followeeId)

    def unfollwo(self,followerId:int,followeeId:int)->None:

        """
        Purpose: unfollow
        """
        if followerId!=followeeId:
            self.followMap[followerId].discard(followeeId)
        
    # end def