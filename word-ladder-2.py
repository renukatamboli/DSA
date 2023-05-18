#User function Template for python3

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        #print("wordlist", wordList, startWord, targetWord)
        wordList = set(wordList)
        queue = []
        queue.append((startWord,))
        usedOnLevel = []
        usedOnLevel.append(startWord)
        level = 0
        ans = []
        while(len(queue)>0):
            vec = queue.pop(0)
            if len(vec) > level:
                level+=1
                #print("usedOnlevel", usedOnLevel, "wordlist", wordList)
                for v in usedOnLevel:
                    if v in wordList:
                        wordList.remove(v)
                usedOnLevel.clear()
            word = vec[-1]
            if word == targetWord:
                if len(ans) == 0:
                    ans.append(list(vec))
                elif len(ans[0]) == len(vec):
                    ans.append(list(vec))
            for i in range(0,len(word)):
                for ch in range(97,123):
                    new_word = str(word[:i] + chr(ch) + word[i+1:])
                    if new_word in wordList:
                        new_vec = vec + (new_word,)
                        queue.append(new_vec)
                        usedOnLevel.append(new_word)
                        new_vec = vec
        return ans
#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends
