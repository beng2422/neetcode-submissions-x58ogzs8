class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic.keys():
                dic[i] = 1
            else:
                 dic[i] = dic[i]+1
        for j in t:
            if j not in dic.keys():
                return False
            else:
                dic[j] = dic[j] - 1
        for i in dic.values():
            if i!=0:
                return False

        return True