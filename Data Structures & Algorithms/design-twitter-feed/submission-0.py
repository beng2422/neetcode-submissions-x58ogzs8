import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followMap = {}

        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1

       # self.tweets.get(userId, []).append([-self.count, tweetId])

        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([-self.count, tweetId])
                

    def getNewsFeed(self, userId: int) -> List[int]:
        
      #  heapq.heapify(self.tweets[userId])
        arr = []
        heapq.heapify(arr)
        j = 0
        # if not self.followMap.get(userId):
        #     return []
        if userId in self.tweets:
            for i in range(len(self.tweets[userId])-1, -1, -1):
                tweet = self.tweets[userId][i]
                heapq.heappush(arr, (-tweet[0], tweet[1]))
                j+=1
                if j==10:
                    break
            

        if userId in self.followMap:
            for followee in self.followMap[userId]:
                if followee not in self.tweets:
                    continue
                for i in range(len(self.tweets[followee])-1, -1, -1):
                    neg_time, tid = self.tweets[followee][i]
                    pos_time = -neg_time
                    heapq.heappush(arr, (pos_time, tid))
                    if len(arr) > 10:
                        heapq.heappop(arr)

        ret = []
        while arr:
            ret.append(heapq.heappop(arr)[1])
        return ret[::-1]


                    






        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return 

        self.followMap.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap :
            self.followMap[followerId].discard(followeeId)

        
