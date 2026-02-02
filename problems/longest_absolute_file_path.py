#https://leetcode.com/problems/longest-absolute-file-path/
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dirs = input.split("\n")
        l = 0
        pwd = ""

        for di in dirs:
            depth = di.count("\t")
            name = di.replace("\t", "")

            # Trim pwd to the correct depth
            while pwd.count("/") > depth:
                pwd = pwd.rsplit("/", 1)[0]

            # Append current directory/file
            pwd += "/" + name

            # If it's a file, update answer
            if "." in name:
                l = max(l, len(pwd) - 1)

        return l
