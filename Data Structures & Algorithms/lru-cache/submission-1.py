class LRUCache:

    def __init__(self, capacity: int):
        self.arr = {}
        self.cap = capacity
        self.currCap = 0
        self.ll = []
        

    def get(self, key: int) -> int:
        return self.arr.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        if val != -1:
            self.arr[key] = value
            return 
        
        if self.currCap<self.cap:

            self.currCap+=1
            self.arr[key] = value
            self.ll.append(key)
        else:
            self.arr.pop(self.ll[0])
            self.ll = self.ll[1:]
            self.arr[key] = value
            self.ll.append(key)

        


        
