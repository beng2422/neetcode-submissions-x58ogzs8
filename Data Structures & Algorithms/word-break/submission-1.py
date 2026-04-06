class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i]=true or false for s[:i]
        #dp[i]=true if there exists word of size j s.t. dp[i-j]==true
        dp = [False for _ in range(len(s)+1)]
        dp[0]=True

        for i in range(len(s)+1):
            for word in wordDict:
                # if i == 8:
                    # print(s[i-len(word):i])

                    # print(dp[i-len(word)])

                if i-len(word)>=0 and s[i-len(word):i] and dp[i-len(word)]:
                    dp[i] = True
        print(dp)
        return dp[len(s)]

            
        