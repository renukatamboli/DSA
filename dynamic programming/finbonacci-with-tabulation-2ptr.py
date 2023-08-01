if __name__ == "__main__":
    prev=0
    prev2=1
    n = 5
    for i in range(2,n+1):
        curri = prev + prev2
        prev = prev2
        prev2 = curri
    print(prev)
