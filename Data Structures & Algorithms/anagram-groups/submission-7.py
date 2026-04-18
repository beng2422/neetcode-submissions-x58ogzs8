from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #alright lets just do this basic
        #create a ret list - if the tuple value is already in the ret list 
        # sdf add it, if not return it
        #

        strsCount = []
        for string in strs:
            x = defaultdict(int)
            for l in string:
                x[l] += 1
            strsCount.append(x)
        def checkEqualHashMaps(hash1, hash2):
            if len(hash1.values()) != len(hash2.values()):
                return False
            for key, val in hash1.items():
                if key not in hash2 or val != hash2[key]:
                    return False
            return True

        #now we iterate through strsCount list and see how often it happens
        retOfDicts = []
        retOfStrings = []

        for indexOfString, stringDict1 in enumerate(strsCount):
            #either existsin ret of dicts or not
            appendedToRet = False
            #see if stringDict2 == stringDict1
            for indexOfRet, stringDict2 in enumerate(retOfDicts):
                if checkEqualHashMaps(stringDict2, stringDict1):
                    retOfStrings[indexOfRet].append(strs[indexOfString])
                    appendedToRet = True
                    break #does this break all loops are just the inner one?


            if not appendedToRet:
                retOfDicts.append(stringDict1)
                retOfStrings.append([strs[indexOfString]])
        return retOfStrings

            


