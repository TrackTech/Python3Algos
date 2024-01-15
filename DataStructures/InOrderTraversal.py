class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# Example usage:
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

def iterative_inorder_traversal(node):

    stack = []
    result = []
    while node or stack:
        while node:
            stack.append(node)
            node=node.left
        
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result

if __name__=="__main__":
    res = iterative_inorder_traversal(root)
    print(res)