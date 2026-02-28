from Create_Tree_Node import list_to_tree
root=list_to_tree([1,2,3,4,None,None,5])
def maxDepth(root):
    if root is None:
        return 0
    left_depth=maxDepth(root.left)
    right_depth=maxDepth(root.right)
    return 1+max(left_depth,right_depth)

print(maxDepth(root))