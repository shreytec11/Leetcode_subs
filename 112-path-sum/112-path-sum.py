# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        
        def dfs(node,cur_sum):
            cur_sum += node.val
            if not node.left and not node.right:
                return targetSum == cur_sum
            
            return (node.left and dfs(node.left, cur_sum)) or (node.right and dfs(node.right, cur_sum))
        
        return dfs(root, 0)