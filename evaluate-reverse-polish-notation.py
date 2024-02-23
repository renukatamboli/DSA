class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+","-","*","/"]
        l = len(tokens)
        if l == 1:
            return int(tokens[0])
        for i in range(l):
            if tokens[i] not in op:
                stack.append(tokens[i])
            else:
                node1 = int(stack.pop())
                node2 = int(stack.pop())
                ans = 0
                if tokens[i] == "+":
                    ans = node1+node2
                if tokens[i] == "-":
                    ans = node2-node1
                if tokens[i] == "/":
                    ans = node2/node1
                if tokens[i] == "*":
                    ans = node2*node1
                stack.append(ans)
        return int(stack[-1])
