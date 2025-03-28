class Solution:

    def add(self,num, arr):
        arr.append(num)
        index = len(arr) - 1
        parent = index // 2

        while arr[parent] > arr[index] and index > 1:
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
            parent = index // 2
    
    def pop(self,arr):
        l = len(arr) - 1
        if l < 1:
            return None
        if l <= 0:
            return
        removed_ele = arr[1]
        arr[1] = arr[-1]
        arr.pop()
        index = 1
        while index*2 < len(arr):
            left = index*2
            right = (index*2)+1
            smallest = left
            if right < len(arr) and arr[right] < arr[left]:
                smallest = right
            if arr[smallest] < arr[index]:
                arr[smallest], arr[index] = arr[index], arr[smallest]
                index = smallest
            else:
                break
        return removed_ele


    def nthUglyNumber(self, n: int) -> int:
        nums = set()
        nums.add(1)
        prime_num = [2,3,5]
        heap = []
        heap.append(-1)
        heap.append(1)
        current_ugly = 1
        for _ in range(n):
            current_ugly = self.pop(heap)
            if not current_ugly:
                return -1
            for prime in prime_num:
                next_ugly = current_ugly * prime
                if next_ugly not in nums:
                    self.add(next_ugly,heap)
                    nums.add(next_ugly)
        return current_ugly



        
        
