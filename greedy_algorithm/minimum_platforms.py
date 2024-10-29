class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        train = []
        platforms = 1
        l = len(arr)
        for i in range(l):
            train.append((arr[i], dep[i],i+1))
        train = sorted(train, key=lambda x: (x[0],x[1], x[2]))
        limits = []
        limits.append(train[0][1])
        for i in range(1,l):
            found = False
            for j in range(len(limits)):
                if train[i][0] > limits[j]:
                    limits[j] = train[i][1]
                    found = True
                    break
            if not found:
                limits.append(train[i][1])
                platforms +=1
        return platforms
