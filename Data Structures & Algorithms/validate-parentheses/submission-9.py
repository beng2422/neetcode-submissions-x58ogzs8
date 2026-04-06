class Solution:
    def isValid(self, s: str) -> bool:




        dictionary = {'(':')', '{': '}', '[':']'}
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

