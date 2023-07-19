#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            pivot = self.partition(arr,low, high)
            self.quickSort(arr, low, pivot-1)
            self.quickSort(arr, pivot+1, high)
        # code here
    
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    def partition(self,arr,low,high):
        i = low
        j = high
        pivot = arr[low]
        while i<j:
            while arr[i] <= pivot and i < high:
                i+=1
            while arr[j] > pivot and j > low:
                j-=1
            if i<j:
                self.swap(arr,i,j)
        self.swap(arr,j,low)
        return j
        # code here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
