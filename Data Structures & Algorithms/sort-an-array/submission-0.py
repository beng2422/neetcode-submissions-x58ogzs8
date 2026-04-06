class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        new = []
        def binarySearch(val, new):
            if not new:
                return [val]
        
            left = 0
            right = len(new)
            while left<right:
                mp = (left+right)//2
                #print(mp)

                if val<=new[mp]:
                    right = mp
                else:
                    left = mp+1

            return new[:left] + [val] + new[left:]





        for i in nums:
            new = binarySearch(i, new)
        return new


 


 