class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        finalIntervals = intervals
        mapIntervals = {}
        print(finalIntervals)
        for i in range(len(finalIntervals)):
            print(finalIntervals[i])
            mapIntervals[finalIntervals[i][0]] = mapIntervals.get(finalIntervals[i][0], [])
            mapIntervals[finalIntervals[i][0]].append(i)

        sortedKeys = sorted(mapIntervals.keys())
        print(sortedKeys)
       # sortedKeys = sortedKeys.dict_keys().sort()
        ints = []
        for i in sortedKeys:
            for j in mapIntervals[i]:
                ints.append(finalIntervals[j])
        res = []
        print(ints)
        curr = ints[0]
        for i in range(1, len(ints)):
            if ints[i][0] <= curr[1]:
                curr[1] = max(curr[1], ints[i][1])
               # i+=1

            else: 
                res.append(curr)
                curr = ints[i]

        res.append(curr)

       # print(finalIntervals)
        return res




        