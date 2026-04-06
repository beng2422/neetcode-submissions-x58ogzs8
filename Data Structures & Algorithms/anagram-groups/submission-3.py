class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create dic: array[dic[]]
        anagrams = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in anagrams:
                anagrams[key] = [i]
            else:
                 anagrams[key] = anagrams[key]+[i]
        return returnList
            
            

            