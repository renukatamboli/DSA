class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        common = ''
        flag = True
        while flag:
            char = ''
            if i < len(strs[0]):
                char = strs[0][i]
            for j in range(1,len(strs)):
                if i < len(strs[j]):
                    if char != strs[j][i]:
                        return common
                    else:
                        continue
                else:
                    return common
            common += char
            i+=1
        return common

