class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dic = {')': '(', '}': '{', ']': '['}
        for i in s:
            #case1: no stack and its a close bracket - return false
            #case2: no stack open bracket
            #case3: stack close bracket - check to see if it closed the val in the stack
            #case4: stack open bracket just append it

            if len(stack)<0:
                if i in dic.keys():
                    return False
                elif i in dic.values():
                    stack.append(i)
                #continue
            else:
                if i in dic.keys():
                    if dic[i] != stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(i)
        if len(stack)>0:
            return False
                
        return True






