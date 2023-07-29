#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
from typing import List


class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        numbers = [i for i in range(1,n+1)]
        permutation = []
        fact=1
        for i in range(1,n):
            fact = fact*i
        k = k-1
        while len(numbers)>0:
            index = k // fact
            permutation.append(numbers[index])
            numbers.pop(index)
            k = k%fact
            if len(numbers)>0:
                fact = fact // len(numbers)
        # code here
        
        return ''.join(str(num) for num in permutation)

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N, K = map(int, input().split())
        
        obj = Solution()
        res = obj.kthPermutation(N, K)
        
        print(res)
        

# } Driver Code Ends
