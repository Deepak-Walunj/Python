class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
def list_to_tree(node):
    if not node:
        return None
    root=TreeNode(node[0])
    i=1
    queue=[root]
    while queue and i<len(node):
        curr=queue.pop(0)
        
        if node[i] is not None:
            curr.left=TreeNode(node[i])
            queue.append(curr.left)
        i+=1
        
        if  i<len(node) and node[i] is not None:
            curr.right=TreeNode(node[i])
            queue.append(curr.right)
        i+=1
        
    return root

def main():
    root=list_to_tree([1,4,6,3,None,4,7,12,None])
    print(root)

if __name__=="__main__":
    main()

