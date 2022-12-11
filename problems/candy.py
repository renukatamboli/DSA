class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1 for i in range(len(ratings))]
        # candies2 = [1]*len(ratings)
        for i in range(0,len(ratings)-1):
            if(ratings[i]>ratings[i+1]):
                candies[i] = candies[i+1]+1
            else:
                if(ratings[i]<ratings[i+1]):
                    candies[i+1]= candies[i]+1

        for j in range(len(ratings)-1,0,-1):
            if(ratings[j]>ratings[j-1] and candies[j]<=candies[j-1]):
                candies[j]= candies[j-1]+1
            else:
                if(ratings[j]<ratings[j-1] and candies[j]>=candies[j-1]):
                    candies[j-1]=candies[j]+1
        # for i in range(0,len(ratings)):
        #     candies[i] = max(candies[i],candies2[i])
        return sum(candies)

        
