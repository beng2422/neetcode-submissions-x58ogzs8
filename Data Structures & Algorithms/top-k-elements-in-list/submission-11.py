class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #
        topKFrequentDict = {}
         
        for i in nums:
            if i in topKFrequentDict.keys():
                topKFrequentDict[i] = topKFrequentDict[i] + 1
            else:
                topKFrequentDict[i] = 1
        topKFrequent = []
        topKFrequentVals = []
        for i in topKFrequentDict.keys():
            val = topKFrequentDict[i]
            if len(topKFrequent) < k:
                topKFrequent.append(i)
                topKFrequentVals.append(val)
            else:
                for j in range(k):
                    min_index = topKFrequentVals.index(min(topKFrequentVals))
                    if val > topKFrequentVals[min_index]:
                        topKFrequent[min_index] = i
                        topKFrequentVals[min_index] = val
        return topKFrequent

            
            
            


        