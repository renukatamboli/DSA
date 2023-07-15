def printf(index,arr,ds,target,s, l):
    if l==index:
        if s==target:
            print("ds",ds)
            return True
        return False
    ds.append(arr[index])
    s+=arr[index]
    if printf(index+1,arr,ds,target,s,l) == True:
        return True
    ds.pop()
    s-=arr[index]
    if printf(index+1,arr,ds,target,s,l) == True:
        return True
    return False    



if __name__ == "__main__":
    arr = [1,2,1]
    ds = []
    target = 2
    printf(0,arr,ds,target,0,3)
