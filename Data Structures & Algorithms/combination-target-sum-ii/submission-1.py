class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(currT, i, path):
            if currT > target:
                return None
            if currT==target:
                if path not in res:


                        res.append( path[:])
            if i>=len(candidates):
                return None
            path.append(candidates[i])
            dfs(currT+candidates[i], i+1, path)
            path.pop()
            dfs(currT, i+1, path)
        dfs(0, 0, [])
        return res  

            





        
        # output = []
        # def recurse(i, currTarget, currList, output):
        #     if currTarget>target:
        #         return []
        #     if currTarget==target:
        #         return currList
            
        #     if i>=len(candidates):
        #         return []
            
        #     rec1 = recurse(i+1, currTarget+candidates[i], currList+[candidates[i]], output)
        #     rec2 = recurse(i+1, currTarget, currList, output)
        #     if len(rec1)>=1:
        #         output+=[rec1]
        #     if len(rec2)>=1:
        #         output+=[rec2]

        #   #  output += [rec1] + [rec2]
        #     return output


        # x = recurse(0, 0, [], [])
        # print(x)
        # newList =[]
        # # for i in x:
        # #     freq = {}
        # #     for j in i:
        # #         freq[j] = freq.get(j, 0) + 1
            
        # #     if freq in newList:


        # seen = set()
        # unique = []
        # for sub in x:
        #     # skip if any element is itself a list
        #     if any(isinstance(e, list) for e in sub):
        #         continue

        #     t = tuple(sub)  # now guaranteed hashable
        #     if t not in seen:
        #         seen.add(t)
        #         unique.append(sub)

        # return unique

        # print(x)


        # return [[]]
            

