#User function Template for python3
class Disjoint:
    def __init__(self, n):
        self.rank   = [0 for i in range(0,n+1)]
        self.size   = [0 for i in range(0,n+1)]
        self.parent = [i for i in range(0,n+1)]
    
    def findUltPar(self,node):
        #print("here", node)
        if node < len(self.parent) and node == self.parent[node]:
            #print("node", node)
            return node
        self.parent[node] = self.findUltPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self,u,v):
        ult_u = self.findUltPar(u)
        ult_v = self.findUltPar(v)
        if ult_u == ult_v:
            return
        if self.rank[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        elif self.rank[ult_u] > self.rank[ult_v]:
            self.parent[ult_v] = ult_u
        else:
            self.parent[ult_u] = ult_v
            self.rank[ult_v]+=1
            
class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        mailNode = {}
        ds = Disjoint(n)
        for i in range(0,n):
            for j in range(1,len(accounts[i])):
                mail = accounts[i][j]
                if mail in mailNode:
                    #print("union,", i, mailNode[mail])
                    ds.unionByRank(i,mailNode[mail])
                else:
                    mailNode[mail] = i
                    
        
        mergedMail = [[] for i in range(0,n)]
        for mail, node in mailNode.items():
            #print("mail", mail, "node", node)
            it = ds.findUltPar(node)
            mergedMail[it].append(mail)
        
        
        ans = []
        
        for i in range(0,n):
             if len(mergedMail[i]) == 0:
                 continue
             else:
                 temp = []
                 temp.append(accounts[i][0])
                 temp = temp + mergedMail[i]
                 temp.sort()
                 ans.append(temp)
        return ans
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends
