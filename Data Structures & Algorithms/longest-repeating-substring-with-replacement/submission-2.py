class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #basically like longest unique substring - but now we keep a pointer of k
        l = 0
        dic = {}
        maxRet = 0
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0)+1


            #sum all values except 
            all_others = sum(list(dic.values())) - max(list(dic.values()))
            while l<=i and k<all_others:
                dic[s[l]] -=1
                l+=1
                all_others = sum(list(dic.values())) - max(list(dic.values()))
            
            if sum(list(dic.values()))>maxRet:
                maxRet = sum(list(dic.values()))
        return maxRet
                



            