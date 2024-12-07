
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        positions = sorted(list(set([x for building in buildings for x in building[0:2]])))

        edge_index_map = {x:i for i,x in enumerate(positions)}

        heights = [0 for _ in range(len(positions))]
        ans = []

        for left,right,height in buildings:

            right_index = edge_index_map[right]
            left_index = edge_index_map[left]

            for i in range(left_index,right_index):
                heights[i] = max(heights[i], height)
        
        for i in range(len(heights)):
            if not (len(ans) > 0 and ans[-1][1] == heights[i]):
                ans.append([positions[i], heights[i]])
        return ans
        
