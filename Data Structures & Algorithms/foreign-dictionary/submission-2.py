from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
    How can we make this a graph problem? 
    An edge: is made between two words a, b find the first letter when they differ  
        '''
        edges = defaultdict(set)
        def createEdges(word1, word2):
            i = 0
            if len(word1) > len(word2) and word1.startswith(word2):
                return False
            while i < len(word1) and i < len(word2):
                if word1[i] != word2[i]:
                    edges[word1[i]].add(word2[i])
                    return True
                i+=1
            return True
        fullWordList = ''.join(words)
        print(set(fullWordList))
        
                    
                



        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not createEdges(words[i], words[j]):
                    return ''
        for i in fullWordList:
            if i not in edges:
                edges[i] = []
        print(edges)
        visited = set()
        visiting = set()
        ret = ''
        def dfs(node):
            nonlocal ret
            if node in visiting:
                print(visiting)
                return False
            if node in visited:
                return True
            visited.add(node)
            visiting.add(node)
            
            for n in edges[node]:
                if not dfs(n):
                    return False
            visiting.remove(node)
            ret += node
         #   ret.append(node)
            return True

            
        keys = edges.keys()
        print(list(keys))
        for i in list(keys):
            if i not in visited:
                if not dfs(i):
                    return ''
        
        ret = list(ret)
        print(ret)
        ret.reverse()
        print(ret)

        return ''.join(ret)







