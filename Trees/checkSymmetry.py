from Create_Tree_Node import list_to_tree
from All_Traversal import preorder, inorder

def isMirror(n1,n2):
    if not n1 and not n2:
        return True
    if not n1 or not n2:
        return False
    return n1.val==n2.val and isMirror(n1.left, n2.right) and isMirror(n1.right,n2.left)
    

def isSymmetric(root):
    if not root:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return isMirror(root.left,root.right)
    
r1=list_to_tree([1,2,2,3,4,4,3])
r2=list_to_tree([1,2,2,None,3,None,3])
print(isSymmetric(r1))
print(isSymmetric(r2))