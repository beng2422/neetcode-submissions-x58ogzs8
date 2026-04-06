class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        left = 0
        ans = ''
        curr_window = {}

#Thoughts- create count of sliding window of s - compare
#subtract each value of count_t
#Create count_t_duplicate, eveerytime you find a fully completed value, you subtract count_t

#OR create count for each sliding window and compare dicts (takes O(1)) - FALSE
#Do the above, and also include values that will let you reach there
#What does the while loop look like though? 
        have = 0
        length =10000000
        
        for i in t:
            count_t[i] = count_t.get(i, 0)+1
        need = len(count_t.keys())
        count_t_dup = count_t
        for i in range(len(s)):
            if s[i] in count_t.keys():
                curr_window[s[i]] = curr_window.get(s[i], 0)+1
                if curr_window[s[i]] == count_t[s[i]]:
                    have+=1
                #print(s[i])
            # if have == need:
                # ans = s[left:i+1]
                # length = i-left+1
            #     print('here')
            #     print('left', left)
            # print("ans", ans, 'have', have, 'need', need)


            while have==need:
                if i-left+1<length:
                    ans = s[left:i+1]
                    length = i-left+1
                # if s[left] not in count_t:
                #     left+=1
                #     ans = s[left:i]
                # elif curr_window.get(s[left], 0)-1>=count_t.get(s[left]):

                #     left+=1
                #     ans[left:i]
                # else:
                #     break
                if s[left] in count_t:
                    curr_window[s[left]] -= 1
                    if curr_window[s[left]] < count_t[s[left]]:
                        have -= 1
                left+=1
            #print(ans)

        return ans




        


        