from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = set(words[0])
        n = len(words)
        adj = defaultdict(list)
        indegree = {}
        ans = []
        queue = []
        for i in range(n-1):
            s1 = words[i]
            s2 = words[i+1]
            letters.update(s1)
            letters.update(s2)
            l1 = len(s1)
            l2 = len(s2)
            l = min(l1,l2)
            index = 0
            flag = 0
            if l1>l2 and s1.startswith(s2):
                return ""
            for j in range(l):
                if s1[j]!=s2[j]:
                    index = j
                    if s2[j] not in adj[s1[j]]:
                        adj[s1[j]].append(s2[j])
                    flag = 1
                    break
                
                
        for letter in letters:
            indegree[letter] = 0
        indegree = dict(sorted(indegree.items()))
        for key in adj:
            adj[key].sort()
            #print("adj",adj)
            for v in adj[key]:
                indegree[v]+=1
        #print("indegree",indegree,"letters",letters)
        for u in indegree:
            if indegree[u] == 0:
                queue.append(u)
                ans.append(u)
        #print("ans",ans,"queue",queue)
        while queue:
            node = queue.pop(0)
            for it in adj[node]:
                indegree[it]-=1
                if indegree[it] == 0:
                    queue.append(it)
                    ans.append(it)
        if len(ans) != len(letters):
            return ""
        return "".join(ans)
                
        
                
        
