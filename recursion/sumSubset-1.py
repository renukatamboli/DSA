# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def findAllSubset(index,s,arr,subset,n):
    if index == n:
        subset.append(s)
        return
    findAllSubset(index+1,s+arr[index],arr,subset,n)
    findAllSubset(index+1,s,arr,subset,n)


if __name__ == '__main__':
    subset = []
    arr = [3,1,2]
    n = len(arr)
    s = 0
    findAllSubset(0,0,arr,subset,n)
    subset.sort()
    print("subset",subset)
