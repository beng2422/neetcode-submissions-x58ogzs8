class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currMin = 0
        left = 0
        ans = 0
        for right in range(len(prices)):
            
            if ans < prices[right]-prices[currMin]:
                 ans = prices[right]-prices[currMin]

            # while left<right:
            #     if ans < prices[right]-prices[left]:
            #         ans = prices[right]-prices[left]
            #     left+=1
            if prices[right]<currMin:
                currMin = prices[right]


        return ans


        