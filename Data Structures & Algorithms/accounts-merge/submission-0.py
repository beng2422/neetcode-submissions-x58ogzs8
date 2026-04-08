from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #idea: put each person into a 

        emailsToIndex = defaultdict(list)
        for index, account in enumerate(accounts):
            for i in range(1, len(account)):
                emailsToIndex[account[i]].append(index)
        
        print(emailsToIndex)
        edges = defaultdict(set)
        for indices in emailsToIndex.values():
            for i in indices:
                for j in indices:
                    edges[i].add(j)
        visited = set()
        def dfs(i, edges):
            visits = set()
            
            queue = [i]
            while queue:
                node = queue.pop(0)
                visits.add(node)
                neighbs = edges[node]
                for i in neighbs:
                    if i not in visits:
                        queue.append(i)
            return visits

        merged = []
        for i in range(len((accounts))):
            if i not in visited:
                out = dfs(i, edges)
                merged.append(out)

                visited = visited | out
        ret = []
        for l in merged:
            emails = set()
            for i in l:
                emails.update(accounts[i][1:])
            emails = sorted(emails)
            ret.append([accounts[next(iter(l))][0]] + emails)
                            





        return ret
        
        
        


