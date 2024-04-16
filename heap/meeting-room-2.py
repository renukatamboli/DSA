class Solution:
    
    def heapSort(self,arr,index,size):
        left = 2*index + 1
        right = 2*index + 2
        largest = index
        
        if left < size and arr[left] > arr[index]:
            largest = left
        
        if right < size and arr[right] > arr[index]:
            largest = right
        
        if largest != index:
            arr[index],arr[largest] = arr[largest],arr[index]
            self.heapSort(arr,largest,size)
        
    def heapify(self,arr):
        size = len(arr)
        
        for i in range(size//2-1,-1,-1):
            self.heapSort(arr,i,size)
        
        for i in range(size):
            arr[0],arr[size-1] = arr[size-1],arr[0]
            size = size-1
            self.heapSort(arr,0,size)
            
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        rooms = []
        rooms.append(intervals[0][1])
        for it in range(1,n):
            if intervals[it][0] < rooms[0]:
                rooms.append(intervals[it][1])
            else:
                rooms[0] = intervals[it][1]
            self.heapify(rooms)
        return len(rooms)
        
        
