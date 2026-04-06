class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        def recurse(open1, close, n, array):

            if open1<close:
                return []
            elif n==0 and open1==close:
                return array
            elif n==0:
                return []
            
            return recurse(open1+1, close, n-1, array+['(']) + recurse(open1, close+1, n-1, array+[')'])
        recursionOutput = recurse(0, 0, 2*n, [])
        retVal = []
        y = ''
        print(recursionOutput)
        for i in range(0, len(recursionOutput)):
            y += recursionOutput[i]
            print(i+1, 2*n)
            if (i+1)%(2*n)==0:
                print('here')
                retVal.append(y)
                y = ''
                


        return retVal



            