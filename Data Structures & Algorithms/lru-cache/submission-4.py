
class Node:
    def __init__(self, val: int, key:int, next1= None, prev= None):
        self.next1 = next1
        self.prev = prev
        self.val = val
        self.key = key
    

class LRUCache:

    


    def __init__(self, capacity: int):
        self.key_val = {}
        self.cap = capacity
        self.ll = None
        self.last = Node(-1, -1)
        self.first = Node(-1, -1)
        self.first.next1 = self.last
        self.last.prev = self.first


    def get(self, key: int) -> int:
        #why a ll works: we only need to keep track of the order - so if its used we move it to the front
        if key in self.key_val:
            #we need to insert the node between the first val and the one to the next
            node = self.key_val[key]
            self.remove(node)
            self.put(key, node.val)




            # pointer_next_node = self.first.next1
            
            # #what about the previous values attached to the node?
            # pointer_prev_next = node.next1
            # pointer_prev_prev = node.prev
            # pointer_prev_next.prev = node.prev
            # pointer_prev_prev.next1 = node.next1


            # #update first dummy pointer, update nodes prev and next vals, update pointer next node prev
            # self.first.next1 = node
            # node.prev = self.first
            # node.next1 = pointer_next_node
            # pointer_next_node.prev = node


            return node.val
        
        return -1


    def remove(self, node):
        if node is self.last or node is self.first:
            return
        node.prev.next1 = node.next1
        node.next1.prev = node.prev
        self.key_val.pop(node.key)



        


    def put(self, key: int, value: int) -> None:
        if key in self.key_val:
            self.key_val[key].val = value
            return 
            
        
        #create node and put pointer in dict
        x = Node(value, key)
        self.key_val[key] = x
        #split the current first val and the values next to it and insert x
        pointer_next = self.first.next1
        self.first.next1 = x #from first to x
        x.prev = self.first 
        x.next1 = pointer_next 
        pointer_next.prev = x
        if len(self.key_val)>self.cap:
            #self.cap-=1
            self.remove(self.last.prev)
























        

        


        
