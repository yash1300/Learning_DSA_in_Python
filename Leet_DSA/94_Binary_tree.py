
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]


class Solution:
    def inorderTraversal(self, root: Optional[Treenode]) -> list[int]:
        if root is None : return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)