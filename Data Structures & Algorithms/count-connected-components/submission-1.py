class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}
        
        for i in edges:
            adjMap[i[0]].append(i[1])
            adjMap[i[1]].append(i[0])
        visited = set()
        def dfs(node):
            queue = [node]

            while queue:
                val = queue[0]
                queue = queue[1:]

                for neighb in adjMap[val]:
                    if neighb not in visited:
                        queue.append(neighb)
                        visited.add(neighb)

            return visited
        num = 0

        for key, val in adjMap.items():
            if key not in visited:
                dfs(key)
                num+=1
            # if val not in visited:
            #     dfs(key)
            #     num+=1
        return num

