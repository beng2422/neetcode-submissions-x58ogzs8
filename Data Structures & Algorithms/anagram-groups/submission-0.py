class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create dic: array[dic[]]
        returnList = []
        for i in range(len(strs)):
            val = strs[i]
            dic = {}
            for i in val:
                if i in dic.keys():
                    dic[i] = dic[i] + 1
                else:
                    dic[i] = 1
            returnList.append(dic)
        returnDic = {}
        returnIndex = {}
        for i in range(len(returnList)):
            dic = returnList[i]
            if dic not in returnDic.keys():
                returnIndex[dic] = [i]
                returnDic[dic] = 1
            else: 
                returnIndex[dic] = returnIndex[dic] = [i]
                returnDic[dic] = returnDic[dic]+1
        returnList1 = []
        for list1 in returnIndex.values():
            returnList.append([strs[i] for i in list1])
        return returnList
            
            

            