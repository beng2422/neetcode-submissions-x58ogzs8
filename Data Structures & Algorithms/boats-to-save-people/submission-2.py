class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #so we can use a greedy approach here -> basically find 2 values that are closest to the limit and keep going there
        #to implement this: we can sort it, then take the largest and match it with the smallest value

        people.sort()
        people.reverse()
        l, r = 0, len(people)-1
        ret = 0
        print(people)
        while l <= r:
            print(l, r, ret)
            if l == r:
                ret += 1
                break
            if people[l] + people[r] > limit:
                ret += 1
                l += 1

            else:
                l +=  1
                r -= 1
                ret += 1 


            


        return ret

