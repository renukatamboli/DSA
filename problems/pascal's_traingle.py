class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        if numRows == 1:
            return ans
        ans.append([1,1])
        if numRows == 2:
            return ans
        numRows=numRows-2
        while numRows != 0:
            cur = ans[-1]
            temp = [1]
            for i in range(len(cur)-1):
                temp.append(cur[i]+cur[i+1])
            temp.append(1)
            ans.append(temp)
            numRows -= 1
        return ans
