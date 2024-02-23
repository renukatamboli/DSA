class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        answers = [0 for i in range(l)]
        stack = []
        stack.append([0,temperatures[0]])
        for i in range(1,l):
            if temperatures[i] > stack[-1][1]:
                while stack and temperatures[i] > stack[-1][1]:
                    node = stack.pop()
                    index = node[0]
                    temp = node[1]
                    answers[index] = i - index
            stack.append([i,temperatures[i]])
        return answers
