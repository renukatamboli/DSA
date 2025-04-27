from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        busy_queue = []
        cur_queue = []
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        for key, value in freq.items():
            heappush(busy_queue, (-value, -n-1 ,key))
        while busy_queue:
            #print("busy here", busy_queue, "cur here", cur_queue)
            node = heappop(busy_queue)
            value = -node[0]
            index = node[1]
            key = node[2]
            #print("key",key,"index", index, "len",len(cur_queue),"n",n,"diff",len(cur_queue) - index)
            if len(cur_queue) - index > n:
                cur_queue.append(key)
                freq[key] -= 1
                if freq[key] > 0:
                    heappush(busy_queue,(-freq[key],len(cur_queue)-1,key))
            else:
                flag = False
                temp_queue = []
                temp_queue.append(node)
                while busy_queue:
                    #print("busy_queue", busy_queue)
                    node = heappop(busy_queue)
                    index = node[1]
                    #print("diff here",len(cur_queue) - index,"len",len(cur_queue))
                    if len(cur_queue) - index > n:
                        key = node[2]
                        cur_queue.append(key)
                        freq[key] -= 1
                        if freq[key] > 0:
                            heappush(busy_queue,(-freq[key],len(cur_queue)-1,key))
                        flag = True
                        break
                    else:
                        temp_queue.append(node)
                for ele in temp_queue:
                    heappush(busy_queue,ele)
                if not flag:
                    cur_queue.append("idle")
        #print("cur_queue", cur_queue)
        return len(cur_queue)
