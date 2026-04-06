class MinStack:

    def __init__(self):
        self.index = 0
        self.array = []
        self.min_stack = []

        

    def push(self, val: int) -> None:
        if len(self.min_stack)==0 or  val<=self.array[self.min_stack[-1]]:
            self.min_stack.append(len(self.array))
        self.array.append(val)
        

    def pop(self) -> None:
        ret = self.array[len(self.array)-1]
        self.array = self.array[:len(self.array)-1]
        if len(self.min_stack) and self.min_stack[len(self.min_stack)-1]==len(self.array):
            self.min_stack = self.min_stack[:len(self.min_stack)-1]
        return ret


        

    def top(self) -> int:
        return self.array[len(self.array)-1]

        

    def getMin(self) -> int:
        if len(self.min_stack)>0:
            return self.array[self.min_stack[-1]]
        else: 
            return 0
        
