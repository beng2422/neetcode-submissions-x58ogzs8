class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create dic: array[dic[]]
        anagram = {}
        for i in strs:
            key = sorted(i)
            if key not in anagrams:
                anagrams[key] = [i]
            else:
                 anagrams[key] = anagrams[key]+[i]
        return returnList
            
            

            