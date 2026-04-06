class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1dict = {}
        s2dict = {}
        for i in range(len(s1)):
            s1dict[s1[i]] = s1dict.get(s1[i], 0) + 1
            s2dict[s2[i]] = s2dict.get(s2[i], 0) + 1
        if s1dict==s2dict:
            return True
        for i in range(len(s1), len(s2)):
            s2dict[s2[i-len(s1)]] =  s2dict.get(s2[i-len(s1)], 0) - 1
            if s2dict[s2[i-len(s1)]]==0:
                s2dict.pop(s2[i-len(s1)])
            s2dict[s2[i]] = s2dict.get(s2[i], 0) + 1
            if s1dict==s2dict:
                return True
        return False
            
            

        