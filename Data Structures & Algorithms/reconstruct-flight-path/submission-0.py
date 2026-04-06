class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #start at jfk, for each neighbor compare lexical order? - what if the correct lexical order doesnt work out?
        #then just use a different order? - kinda like backtracking?
        ret = []
        stack  = ['JFK']
        visited = set()
        while stack:
            node = stack.pop()
            ret.append(node)
            neighbs = []
            
            for i, ticket in enumerate(tickets):
                if node==ticket[0] and i not in visited:
                    visited.add(i)
                    neighbs.append(ticket[1])
            neighbs.sort()
            neighbs = neighbs[::-1]
            print(neighbs)
            stack = stack + neighbs
        
            print


        return ret






