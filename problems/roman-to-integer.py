class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sys_map = dict()
        sys_map["I"] = 1
        sys_map["V"] = 5
        sys_map["X"] = 10
        sys_map["L"] = 50
        sys_map["C"] = 100
        sys_map["D"] = 500
        sys_map["M"] = 1000

        integer = 0
        for i in range(0,len(s)-1):
            if (sys_map[s[i]] >= sys_map[s[i+1]]):
                integer+= sys_map[s[i]]
            else:
                integer -= sys_map[s[i]]
        integer += sys_map[s[len(s)-1]]
        return integer
