import re
from collections import defaultdict
class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        #queue = []
        #l = len(replacements)
        #adj = defaultdict(list)
        #indegree = defaultdict(int)
        text_r = {}
        #order = {}
        #keys = []
        for replacement in replacements:
        #    keys.append(replacement[0])
            text_r[replacement[0]] = replacement[1]
        #     matches = re.findall(r'%[A-Z]%', replacement[1])
        #     for match in matches:
        #         adj[replacement[0]].append(match[1])    
        #         indegree[match[1]] += 1
        # for i in keys:
        #     if indegree[i] == 0:
        #         queue.append(i)
        #         order[i] = []
        # while queue:
        #     node = queue.pop(0)
        #     for v in adj[node]:
        #         indegree[v]-=1
        #         if indegree[v] == 0:
        #             queue.append(v)
        #             order[node].append(v)
        matches = re.findall(r'%[A-Z]%', text)
        while matches:
            for match in matches:
                text = text.replace(match, text_r[match[1]])
            matches = re.findall(r'%[A-Z]%', text)
        return text
        



        
