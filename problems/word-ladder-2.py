class Solution(object):
    def __init__(self):
        self.b = ""
        self.ans = []
        self.mmap = dict()

    def dfs(self, word, seq):
        if word == self.b:
            seq.reverse()
            self.ans.append(seq)
            return
        steps = self.mmap[word]
        for i in range(0,len(word)):
            for ch in range(97,123):
                new_word = str(word[:i] + chr(ch) + word[i+1:])
                #print("new_word", new_word,"steps",self.mmap.get(new_word,""),"s", steps, seq)    
                if new_word in self.mmap and self.mmap[new_word] + 1 == steps:
                        #print("here","new_word", new_word,"steps",self.mmap.get(new_word,""),"s", steps) 
                        seq.append(new_word)
                        new_seq = seq[:]
                        self.dfs(new_word,new_seq)
                        seq.pop()


    def findLadders(self, beginWord, endWord, wordList):
        self.b = beginWord
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        queue = []
        queue.append(beginWord)
        self.mmap[beginWord] = 0
        while(len(queue)>0):
            word = queue.pop(0)
            steps = self.mmap[word]
            for i in range(0,len(word)):
                for ch in range(97,123):
                    new_word = str(word[:i] + chr(ch) + word[i+1:])
                    #print("new_word",new_word)
                    if new_word in wordList:
                        #print("here","new_word", new_word,self.mmap)
                        queue.append(new_word)
                        self.mmap[new_word] = steps+1
                        wordList.remove(new_word)
        if endWord in self.mmap:
            seq = []
            seq.append(endWord)
            self.dfs(endWord, seq)

        return self.ans
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
