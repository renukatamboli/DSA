def permutations(arr,ans,ds,hashmap):
    if len(ds)==len(arr):
        ans.append(ds[:])
        return
    
    for i in range(0,len(arr)):
        if not hashmap[i]:
            hashmap[i] = True
            ds.append(arr[i])
            permutations(arr,ans,ds,hashmap)
            ds.pop()
            hashmap[i] = False

ans = []
arr  =[1,2,3]
hashmap = [False for i in range(0,len(arr))]
ds = []
permutations(arr,ans,ds,hashmap)
print("ans",ans)
