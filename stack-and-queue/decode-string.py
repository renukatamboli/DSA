class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                if s[i] == "]":
                    chars = []
                    nums = []
                    while stack[-1] != "[":
                        node = stack.pop()
                        chars.append(node)
                    stack.pop()
                    while stack and stack[-1] != "[" and not stack[-1].isalpha():
                        node = stack.pop()
                        nums.append(node)
                    chars.reverse()
                    nums.reverse()
                    chars = ''.join(chars)
                    nums = ''.join(nums)
                    formedStr = ''
                    for i in range(int(nums)):
                        formedStr+=chars
                    stack.append(formedStr)
        return ''.join(stack)
