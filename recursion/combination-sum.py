# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def combinations(index,arr,target,ans,ds):
    if index==len(arr):
        if target==0:
            ans.append(ds[:])
        return
    
    if arr[index] <= target:
        ds.append(arr[index])
        combinations(index,arr,target-arr[index],ans,ds)
        ds.pop()
    combinations(index+1,arr,target,ans,ds)
    

ans = []
arr  =[2,3,6,7]
ds = []
combinations(0,arr,7,ans,ds)
print("ans",ans)
