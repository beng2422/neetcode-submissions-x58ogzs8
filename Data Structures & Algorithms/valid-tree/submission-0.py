class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Ideas: we can run dfs and see if it creates a cycle
        #prims?
        stack = [(0, -1)]
        seen = set()


        #issue right now - fails because it goes right back
        while stack:
            node, parent = stack.pop()
            seen.add(node)
           # print(node)
            for i in range(len(edges)):
                edge = edges[i]
                
                    
                if node in edge:
                    x, y = edge[0], edge[1]
                    print('x', x, 'y', y, 'node', node)
                    x, y = edge[0], edge[1]

                    if x==node:
                        if y == parent:
                            continue
                        if y in seen:
                            return False
                        
                        
                        stack.append((y, x))
                    else:
                        if x==parent:
                            continue
                        if x in seen:
                            return False

                        stack.append((x, y))
            
        return True


    
    