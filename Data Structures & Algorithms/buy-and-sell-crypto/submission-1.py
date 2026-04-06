class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currMin = 1000000
        left = 0
        ans = 0
        for right in range(len(prices)):
            
            if ans < prices[right]-currMin:
                 ans = prices[right]-currMin

            # while left<right:
            #     if ans < prices[right]-prices[left]:
            #         ans = prices[right]-prices[left]
            #     left+=1
            if prices[right]<currMin:
                currMin = prices[right]

        print(currMin)
        return ans


        