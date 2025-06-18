import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r'\/\/\/', '/', path)
        path = re.sub(r'\/\/', '/', path)
        directories = path.split("/")
        ans = ''
        for i in range(len(directories)):
            if directories[i] == "":
                continue
            if directories[i] == ".":
                continue
            elif directories[i] == "..":
                count = 0
                for i in range(len(ans)-1,-1,-1):
                    if ans[i] == '/':
                        break
                ans = ans[:i]
            else:
                ans+= "/" + directories[i]
        if ans == "":
            return "/"
        return ans
            
