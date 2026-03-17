from collections import defaultdict

class Solution:
    def killProcess(self, pid, ppid, kill):
        adj = defaultdict(list)
        
        for i in range(len(ppid)):
            adj[ppid[i]].append(pid[i])
        
        ans = []
        stack = [kill]
        
        while stack:
            node = stack.pop()
            ans.append(node)
            
            for child in adj[node]:
                stack.append(child)
        
        return ans
