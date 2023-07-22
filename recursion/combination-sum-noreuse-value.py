# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def combinations(index,arr,target,ans,ds):
    if target==0:
        ans.append(ds[:])
        return
    for i in range(index,len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        if arr[i] <= target:
            ds.append(arr[i])
            combinations(i+1,arr,target-arr[i],ans,ds)
            ds.pop()
    

ans = []
arr  =[1,1,1,2,2]
ds = []
combinations(0,arr,3,ans,ds)
print("ans",ans)
