def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def permutations(index,arr,ans):
    if len(arr) == index:
        ans.append(arr[:])
        return
    
    for i in range(index,len(arr)):
        swap(arr,index,i)
        permutations(index+1,arr,ans)
        swap(arr,index,i)


if __name__ == '__main__':
    arr = [1,2,3]
    ans = []
    permutations(0,arr,ans)
    print("ans",ans)
