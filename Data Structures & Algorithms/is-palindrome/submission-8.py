class Solution:
    def isPalindrome(self, s: str) -> bool:
        #idea have 2 pointers that check if each value is equal until it meets in the midele
        #first we need to get rid of all non-alphanumeric characters
        newS = ""
        #alphaNumeric = set((1,2,3,4,5,6,7,8,9, "A", "B", C))
        for i in s:
            if i.isalnum():
                newS+=i
        
        for i in range(len(newS)//2):
            if newS[i].lower()!=newS[len(newS)-1-i].lower():
                return False
        return True

