class CountSquares:

    def __init__(self):
        self.list1 = {}
        

    def add(self, point: List[int]) -> None:
        self.list1[(point[0], point[1])] = self.list1.get((point[0], point[1]), 0) + 1

        

    def count(self, point: List[int]) -> int:
        diag = []
        res = 0
        for x,y in self.list1: 
            if abs(point[0] + x) == abs(point[1] + y):
                diag.append((x,y))
                if (point[0], y) in self.list1 and (x, point[1]):
                    res+=self.list1[(point[0], y)] * self.list1[(x, point[1])]*self.list1[(x,y)]
        return res
        

        
