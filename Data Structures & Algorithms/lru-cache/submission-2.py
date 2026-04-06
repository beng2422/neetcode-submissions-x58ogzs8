class LRUCache:

    def __init__(self, capacity: int):
        self.arr = {}
        self.cap = capacity
        self.currCap = 0
        self.ll = []
        

    def get(self, key: int) -> int:
        if key not in self.arr:
            return -1
        self.ll.remove(key)
        self.ll.append(key)
        return self.arr.get(key)
        

    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        if val != -1:
            self.arr[key] = value
            self.ll.remove(key)
            self.ll.append(key)
            return 
        
        if self.currCap<self.cap:

            self.currCap+=1
            self.arr[key] = value
            self.ll.append(key)
        else:
            lru = self.ll.pop(0)
            self.arr.pop(lru)

            self.arr[key] = value
            self.ll.append(key)

        


        
