#User function Template for python3

import sys
class Solution:

    def kthElement(self, a, b, k):
        n1 = len(a)
        n2 = len(b)
        if n1 > n2:
            return self.kthElement(b,a,k)
        n = n1+n2
        low = max(0,k-n2)
        high = min(k,n1)
        left = k
        while low <= high:
            mid1 = (low+high) // 2
            mid2 = left - mid1
            l1 = - sys.maxsize - 1 
            l2 = - sys.maxsize - 1
            r1 = sys.maxsize
            r2 = sys.maxsize
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1-1 >= 0:
                l1 = a[mid1-1]
            if mid2-1 >= 0:
                l2 = b[mid2-1]
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2)
            if l1 > r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
