class Solution(object):
    def DFS(self,sr,sc,ans, image, color, initColor):
        deltaRow = [1, 0, -1, 0]
        deltaCol = [0, 1, 0, -1]
        ans[sr][sc] = color
        for i in range(0,4):
            nRow = sr+deltaRow[i]
            nCol = sc+deltaCol[i]
            if(nRow>=0 and nRow<len(image) and nCol>=0 and nCol<len(image[0]) and image[nRow][nCol] == initColor and ans[nRow][nCol] != color):
                self.DFS(nRow, nCol, ans,image, color, initColor)
            
    def floodFill(self, image, sr, sc, color):
        initColor = image[sr][sc]
        ans = image[:]
        self.DFS(sr,sc,ans, image, color, initColor)
        return ans
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
