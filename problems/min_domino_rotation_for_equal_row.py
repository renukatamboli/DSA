from collections import defaultdict
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counter = defaultdict(int)
        for top in tops:
            counter[top] += 1
        for bottom in bottoms:
            counter[bottom] += 1
        maxi = 0
        ele = -1
        for key, value in counter.items():
            if value > maxi:
                ele = key
                maxi = value
        count = 0
        topCount = tops.count(ele)
        bottomCount = bottoms.count(ele)
        for i in range(len(tops)):
            if tops[i] != ele and bottoms[i] != ele:
                return -1
            elif tops[i] == ele and bottoms[i] == ele:
                continue
            else:
                if topCount >= bottomCount and tops[i] != ele and bottoms[i] == ele:
                    count+=1
                elif topCount < bottomCount and tops[i] == ele and bottoms[i] != ele:
                    count+=1
        return count
