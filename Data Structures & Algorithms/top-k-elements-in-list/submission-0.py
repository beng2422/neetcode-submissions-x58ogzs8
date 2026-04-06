class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topKFrequent = {}
        for i in nums:
            if i in topKFrequent.keys():
                topKFrequent[i] = topKFrequent[i] + 1
            else:
                topKFrequent[i] = 1
        
        return [i for i in topKFrequent.keys()][:k]

        