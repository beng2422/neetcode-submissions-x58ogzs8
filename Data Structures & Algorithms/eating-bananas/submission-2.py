class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        if h<len(piles):
            return None
        minimumK = r
        while l<=r:
            k = (r+l)//2
            hGuess = 0
            print('right', r, 'left', l, 'k',k)
            for i in piles:
                if i%k == 0:

                    hGuess = hGuess + i//k
                else: 
                    hGuess = hGuess + i//k+1
                print('i', i, 'hguess', hGuess)
            print('hguess', hGuess)
            if hGuess>h:
                l = k+1
                
            else:
                r= k-1
                minimumK = k
            

        return minimumK