from Create_Tree_Node import list_to_tree
from All_Traversal import inorder
def isSameTree(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None :
        return False
    if root1.val==root2.val:
        return isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)

r1=list_to_tree([0,1])
r2=list_to_tree([0])
# print(inorder(r1))
print(isSameTree(r1,r2))