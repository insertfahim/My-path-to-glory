# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minimumvaluenode(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def delete(root,val):
            if not root:
                return None
            if val>root.val:
                root.right=delete(root.right,val)
            elif val<root.val:
                root.left=delete(root.left,val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    mininode = minimumvaluenode(root.right)
                    root.val=mininode.val
                    root.right = delete(root.right,mininode.val)
            return root
        return delete(root,key)