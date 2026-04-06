class Solution:
    def validPalindrome(self, s: str) -> bool:


        def tryRightMove():
            left = 0
            right = len(s)-1
            one = 0
            while left<right:
                if s[left]!=s[right] and one==1:
                    return False
                if s[left] != s[right]:
                    one = 1
                    right-=1
                else:
                    right-=1
                    left+=1
            return True
        def tryLeftMove():
            left = 0
            right = len(s)-1
            one = 0
            while left<right:
                print(s[left], s[right], one)
                if s[left]!=s[right] and one==1:
                    return False
                if s[left] != s[right]:
                    one = 1
                    left+=1
                else:
                    right-=1
                    left+=1
            return True

        return tryLeftMove() or tryRightMove()


        