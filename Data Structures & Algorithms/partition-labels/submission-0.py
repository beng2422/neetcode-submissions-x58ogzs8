class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        curr = ''
        for i, val in enumerate(s):

            if val in s[:i]:
                for j in range(len(output)):
                    if j>=len(output):
                        break
                    
                    if val in output[j]:
                        print('current val is equal in output[j]', j)
                        newVal = ''
                        print('attempting to modify output and append newVal')
                        for k in range(j, len(output)):
                            print('k', k)
                            sub = output[k]
                            newVal = newVal + sub
                        output = output[:j]
                        output.append(newVal + val)
                        print('newVal', newVal+val)
                    
                        
            else:
                output.append(val)
            print('full output', output)
        res = []
        for sub in output:
            res.append(len(sub))

        return res



            
