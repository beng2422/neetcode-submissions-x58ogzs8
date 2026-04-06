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
                topKFrequentVals(val)
            else:
                for j in topKFrequentVals:
                    if j<val:
                        topKFrequent = topKFrequent[:j] + i + topKFrequent[j+1:]
                        topKFrequentVals = topKFrequentVals[:j] + val + topKFrequentVals[j+1:]
                        continue
        return topKFrequent

            
            
            


        