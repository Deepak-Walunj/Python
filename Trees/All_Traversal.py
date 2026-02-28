from Create_Tree_Node import list_to_tree

def inorder(root):
    ls=[]
    def traversal(node):
        if not node:
            return
        traversal(node.left)
        ls.append(node.val)
        traversal(node.right)
        
    traversal(root)
    return ls
def preorder(root):
    ls=[]
    def traversal(node):
        if not node:
            return
        
        ls.append(node.val)
        traversal(node.left)
        traversal(node.right)
        
    traversal(root)
    return ls
def postorder(root):
    ls=[]
    def traversal(node):
        if not node:
            return
        traversal(node.left)
        traversal(node.right)
        ls.append(node.val)
        
    traversal(root)
    return ls

def main():
    root=list_to_tree([1,4,6,3,None,4,7,12,None])
    # print(root)
    inOr=inorder(root)
    print(inOr)
    preOr=preorder(root)
    print(preOr)
    posOr=postorder(root)
    print(posOr)
if __name__=="__main__":
    main()