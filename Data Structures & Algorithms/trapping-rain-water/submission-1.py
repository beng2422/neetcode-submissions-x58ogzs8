class Solution:
    def trap(self, height: List[int]) -> int:
        #First thoughts - I could probably do the max_heights question - it seems like a good variation
        #Our data struc could be from right to left and keep track of current max height and res (area trapped)
        #Once we hit a val that is smaller than height we update res, if its larger or eq we update current max height

        #heightVal - lowVal 

        res = 0
        mapping = {}
        curr_max_height = 0
        curr_max_ind = 0
        curr_low_ind = 0
        i = 0
        
        while i<len(height) and height[i] == 0:
            
            i+=1
        curr_max_height = height[i]
        curr_max_ind = i
        print(i)
        last_res = 0
            

        while i < len(height):

           

            if height[i]>=curr_max_height:
                curr_max_height = height[i]
                last_res = 0
            else:
                last_res += ( curr_max_height - height[i]) 
                res +=( curr_max_height - height[i]) 

            print('i', i, 'res', res)
            i+=1
        
            
        return res - last_res


