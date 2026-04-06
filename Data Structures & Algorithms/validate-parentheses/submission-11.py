class Solution:
    def isValid(self, s: str) -> bool:
        #alright we want to do this simply and elegantly and not make it a mess
        #what we can do is make this a stack and 
        #we will have a for loop iterate through it and pop the last value of the stack
        #if a dict.value is added that we dont know about, return false

        dictionary = {'(':')', '{': '}', '[':']'}
        stack = [s[0]]
        if s[0] not in dictionary.keys():
            return False
        for i in range(1, len(s)):
            if len(stack)>0:
                last_val = stack.pop()
            else:
                last_val = None

            #check if its a valid parantheses
            if s[i] in dictionary.values() and last_val and dictionary[last_val] == s[i]:
                print('good')

            elif s[i] in dictionary.values() and last_val and dictionary[last_val] != s[i]:
                return False
            elif s[i] not in dictionary.values():
                stack.append(last_val)
                stack.append(s[i])
            











        if s[0] not in dictionary.keys():
            return False
        stack = [s[0]]
        
        s = s[1:]
        while stack and s:
            stack_val = stack.pop()
            ending = s[0]
            print('stack_val', stack_val)
            print('ending', ending)
            if ending in dictionary.values():
                print(dictionary[stack_val] == ending)
                if dictionary[stack_val] != ending:
                    print('here')
                    return False
                
            else:

                stack.append(stack_val)
                stack.append(ending)
            s = s[1:]

        # if len(stack)>0 or len(s)>0:
        #     return False
        return True


        # stack = []
        # dictionary = {'(':')', '{': '}', '[':']'}
        # rest = ''
        # for i in range(len(s)):
        #     print(i)
        #     if s[i] in ['(', '{', '[']:
        #         stack.append(s[i])
        #     elif s[i] in [')', '}', ']']:
        #         rest = s[i:]
        #         break
        # print('stack', stack)

        # while stack and rest: 
        #         x = stack.pop()
        #         y = rest[0]
        #         rest = rest[1:]
        #         print(x, y)

        #         if dictionary[x]==y:
        #             continue
        #         else:
        #             return False
        # if len(stack)>0 or len(rest)>0:
        #     return False
        # return True 

