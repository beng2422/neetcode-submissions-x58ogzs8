class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #a subsequence is just the list of characters that are in the same order 

        #dp[i][j] = largest length of common subsequence 
        #dp[i][j] = max (dp[i][j-1] + 1 if text2[j-1]==text1[i], dp[i-1][j] +1 if text1[i-1]==text2[j]



        #dp[i][j] = dp[i-1][j-1]+1 if text1[i-1]==text2[j-1] else max(dp[i-1][j], dp[i][j-1])


        
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for j in range(1, len(text1)+1):
            for i in range(1, len(text2)+1):
                if text1[j-1]==text2[i-1]:
                    print('here', text1[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[len(text2)][len(text1)]