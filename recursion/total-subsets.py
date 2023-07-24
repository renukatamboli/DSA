# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def findAllSubset(index,ds,arr,ans,n):
    for i in range(index,n):
        if i != index and arr[i] == arr[i-1]:
            continue
        ds.append(arr[i])
        findAllSubset(i+1,ds,arr,ans,n)
        ds.pop()
    ans.append(ds[:])

if __name__ == '__main__':
    arr = [3,1,2]
    n = len(arr)
    ds = []
    ans = []
    findAllSubset(0,ds,arr,ans,n)
    print("subset",ans)
