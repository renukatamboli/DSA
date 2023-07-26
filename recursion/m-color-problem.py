def isSafe(node,g,color,n,col):
    for it in g[node]:
        if color[it] == col:
            return False
    return True

def solve(node,g,color,n,m):
    if node == n:
        return True
    
    for i in range(1,m):
        if isSafe(node,g,color,n,i):
            color[node] = i
            if solve(node+1,g,color,n,m):
                return True
            color[node] = 0


if __name__ == "__main__":
    g = [[1,3],[0,2],[1,3],[0,2]]
    n = 4
    m = 1
    color = [0 for i in range(1,n+1)]
    if solve(0,g,color,n,m) == True:
        print("True")
    else:
        print("False")
