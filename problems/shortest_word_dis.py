class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dis = 1e9
        index1 = -1
        index2 = -1
        for index,word in enumerate(wordsDict):
            if word == word1:
                index1 = index
            if word == word2:
                index2 = index
            if index1 != -1 and index2 != -1:
                dis = min(dis,abs(index1-index2))
        return dis
         
