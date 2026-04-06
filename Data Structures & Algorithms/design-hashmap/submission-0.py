class MyHashMap:

    def __init__(self):
        self.k = []
        self.v = []
        

    def put(self, key: int, value: int) -> None:
        if key in self.k:
            self.v[self.k.index(key)] = value
        else:

            self.k.append(key)
            self.v.append(value)


        

    def get(self, key: int) -> int:
        print(self.v)
        print(self.k)
        print(key)
      #  print(self.k.index(key))
        if key in self.k:
            return self.v[self.k.index(key)] 
        
        return -1


    def remove(self, key: int) -> None:
        if key in self.k:
            self.v = self.v[:self.k.index(key)] + self.v[self.k.index(key)+1:]
            self.k = self.k[:self.k.index(key)] + self.k[self.k.index(key)+1:]












        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)