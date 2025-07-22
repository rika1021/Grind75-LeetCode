# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        if root is None:
            return None
        
        temp = root.left
        root.left=root.right
        root.right=temp

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root
    

#【 文法訂正 】

# 1. 遞迴調用缺少 self
#     self.invertTree()
# 2. Python 使用點運算符 . 來訪問物件的屬性
#     root.left