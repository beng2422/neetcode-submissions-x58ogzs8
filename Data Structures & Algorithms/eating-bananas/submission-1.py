class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        #start at m, try and see if it works, if it doesnt try again
        left = 1
        right = max(piles)
        
        while left<right:
            mid =( left+right) //2

            hours = 0
            for i in range(len(piles)):
                hours += ((piles[i]+mid-1)//mid)

            if hours>h:
                left = mid+1
            else:
                right = mid
        return left
        

