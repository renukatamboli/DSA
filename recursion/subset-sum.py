def printf(index,arr,ds,target,s, l):
    if l==index:
        if s==target:
            print("ds",ds)
        return
    ds.append(arr[index])
    s+=arr[index]
    printf(index+1,arr,ds,target,s,l)
    ds.pop()
    s-=arr[index]
    printf(index+1,arr,ds,target,s,l)



if __name__ == "__main__":
    arr = [1,2,1]
    ds = []
    target = 2
    printf(0,arr,ds,target,0,3)
