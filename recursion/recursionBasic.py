def printf(index,arr,ds,n):
    if index==n:
        print("ds",ds)
        return
    ds.append(arr[index])
    printf(index+1,arr,ds,n)
    ds.pop()
    printf(index+1,arr,ds,n)



if __name__ == "__main__":
    arr = [3,1,2]
    ds = []
    printf(0,arr,ds,3)
