from typing import Optional
class TreeNode:
    def __init__(self,val:int,left:Optional['TreeNode']=None,right:Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(node):
    stack = []
    prev = None

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        
        prevVal = -1

        if prev:
            #print("previous node - ",prev.val)
            prevVal = prev.val
        print("Current Val-",node.val, ", Previous val=",prevVal)
        prev = node
        node = node.right


def main():

    node = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(5))
    traverse(node)
    
if __name__ == "__main__":
    main()
    