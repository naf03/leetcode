# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, targetSum, runningSum):
            if not node:
                return False
            runningSum+=node.val
            #found a leaf
            if not node.left and not node.right:
                if runningSum == targetSum:
                    return True
                else:
                    return False
            if dfs(node.left, targetSum, runningSum):
                return True
            if dfs(node.right, targetSum, runningSum):
                return True
            return False
        return dfs(root, targetSum, 0)


            
        