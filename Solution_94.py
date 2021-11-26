"""
94. Binary Tree Inorder Traversal
Easy

6213

262

Add to List

Share
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
Accepted
1,221,877
Submissions
1,769,541
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        res+=self.inorderTraversal(root.left)
        res.append(root.val)
        res+=self.inorderTraversal(root.right)
        return res

if __name__ == '__main__':
    so = Solution()
    print(so.inorderTraversal([1,2,3]))

    """
    没看懂题目还是
    
    
    对于二叉树：
        有深度遍历 和 广度遍历
        深度遍历有：前序，中序，后序 三种； 可以递归解决
        广度遍历即：层次遍历 ；           需要借助其他数据结构支撑，e.g.，堆
        
    遍历思想：
        前序：根结点-》左子树-》右子树
        中序：左子树-》根结点-》右子树
        后续：左子树-》右子树-》根结点
        层次遍历：按层次遍历即可
    
        
        
    """



