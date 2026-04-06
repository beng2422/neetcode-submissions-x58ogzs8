class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict where val = a num that is repeated key number of times
        # We can 
        topKFrequentDict = {}
         
        for i in nums:
            if i in topKFrequentDict.keys():
                topKFrequentDict[i] = topKFrequentDict[i] + 1
            else:
                topKFrequentDict[i] = 1
        topKFrequentDictReversed = {}
        for i in topKFrequentDictReversed.keys():
            val = topKFrequentDictReversed[i]
            if val in topKFrequentDictReversed.keys():
                topKFrequentDictReversed[val].append(i)
            else:
                topKFrequentDictReversed[val] = [i]
        ret = []
        for i in range(len(nums), 0, -1):
            if i in topKFrequentDictReversed:
                for x in topKFrequentDictReversed[i]:
                    if len(ret) > k:
                        ret.append(x)
                    else:
                        return ret

        return ret
            
            
            

            
        

            
            


        