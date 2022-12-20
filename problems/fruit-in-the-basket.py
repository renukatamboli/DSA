import collections
class Solution(object):
    def totalFruit(self, fruits):
        max_fruits = 0
        left=0
        right=0
        index =0
        fruit_combo = collections.OrderedDict()
        for i in range(0,len(fruits)):
            if(fruits[i]!=fruits[i-1]):
                if(len(fruit_combo)==2):
                    fruit_combo.popitem(last = False)
                fruit_combo[fruits[i]]= i
            if(len(set(fruits[left:right+1]))>2):
                left = fruit_combo.items()[0][1]
            max_fruits = max(max_fruits,right-left+1)
            right+=1
        return max_fruits
