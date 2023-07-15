def printf(index,arr,target,s, l):
    if l==index:
        if s==target:
            return 1
        return 0
    s+=arr[index]
    le = printf(index+1,arr,target,s,l)
    s-=arr[index]
    re = printf(index+1,arr,target,s,l) 
    return le + re



if __name__ == "__main__":
    arr = [1,2,1]
    ds = []
    target = 2
    ans = printf(0,arr,target,0,3)
    print("ans",ans)
