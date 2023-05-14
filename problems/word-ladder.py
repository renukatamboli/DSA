class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        queue = []
        queue.append((beginWord,1))
        wordList = set(wordList)
        while(len(queue)>0):
            wordInfo = queue.pop(0)
            word = wordInfo[0]
            steps = wordInfo[1]
            if word == endWord:
                return steps
            for i in range(0,len(word)):
                for ch in range(97,123):
                    new_word = str(word[:i] + chr(ch) + word[i+1:])
                    if new_word in wordList:
                        queue.append((new_word,steps+1))
                        wordList.remove(new_word)
        return 0
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
