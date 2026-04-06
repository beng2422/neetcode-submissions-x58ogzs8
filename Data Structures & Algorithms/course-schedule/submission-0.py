class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if a cycle exists return false
        #Run dfs- [[0,1,2,3], [3, 4, 0]]
        #0-1-2-3.  3-4-0
        #just check if there exists a pair that is reversed in one list

        #{(0,1)}
        new_tuple_set = set()
        for i in prerequisites:
            for j in range(len(i)):
                x = 1
                while j<x<len(i):
                    if (i[x], i[j]) in new_tuple_set:
                        return False
                    new_tuple_set.add((i[j], i[x]))
                    x+=1

        return True

        # {0: [1,2,3], 1:[2,3], 2:[3]}



        # def dfs(prerequisites):
        #     stack = prerequisites[0]
        #     visited = set()

        #     while stack:
        #         node = stack.pop()
                

        #         if node not in visited:
        #             visited.add(node)


                    
                
                
                