class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for i in digits:
            res += str(i)
        newRes = int(res) + 1
        resList = []
        for i in str(newRes):
            resList.append(int(i))
        return resList

        