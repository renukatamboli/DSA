from collections import defaultdict
from typing import List

class Solution:
    def __init__(self):
        self.root = {}
        self.rank = defaultdict(int)
        self.lsts = defaultdict(list)

    def find(self, x):
        if self.root[x][0] != x:
            self.root[x][0] = self.find(self.root[x][0])
        return self.root[x][0]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY][0] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX][0] = rootY
        else:
            self.root[rootY][0] = rootX
            self.rank[rootX] += 1

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in self.root:
                    self.root[email] = [email, name]

        for account in accounts:
            for i in range(1, len(account) - 1):
                self.union(account[i], account[i + 1])

        for email in self.root:
            root_email = self.find(email)
            self.lsts[root_email].append(email)

        result = []
        for root_email, emails in self.lsts.items():
            name = self.root[root_email][1]
            result.append([name] + sorted(emails))
        return result
