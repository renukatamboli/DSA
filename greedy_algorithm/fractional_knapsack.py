class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, values, weights, w):
        entries = []
        l = len(values)
        for i in range(l):
            entries.append((weights[i],values[i]))
        entries = sorted(entries,key = lambda x:(x[0]/x[1]))
        i = 0
        profit = 0
        while w > 0 and i < l:
            if w >= entries[i][0]:
                w -= entries[i][0]
                profit += entries[i][1]
            else:
                p = (entries[i][1] * w) / entries[i][0]
                profit += p
                w = 0
            i+=1
        return profit
