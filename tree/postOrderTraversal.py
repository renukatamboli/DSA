class Solution:
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        visited = set()
        stack.append(root)
        if root is None:
            return ans
        while len(stack) > 0:
            cur = stack[-1]
            while cur not in visited:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                visited.add(cur)
                cur = stack[-1]
            temp = stack.pop()
            ans.append(temp.val)
        return ans
