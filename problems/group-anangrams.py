#solution with m * n logn complexity
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(string)
        return anagrams.values()
        

 #another solution with 26*m*n complexity
        
 class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()
        for string in strs:
            counter = [0] * 26
            for i in string:
                counter[ord(i)-97] += 1
            count_str = "#".join(str(x) for x in counter)
            if count_str not in anagrams:
                anagrams[count_str] = []
            anagrams[count_str].append(string)
        return anagrams.values()
        
