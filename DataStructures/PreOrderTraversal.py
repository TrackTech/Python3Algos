class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def iterative_preorder_traversal(root):
    if not root:
        return []
    
    print("Root is-",root.val)

    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        result.append(current.val)

        # Push the right child first so that left child is processed first (since it's a stack)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result
# root -> root.left -> root.right
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

if __name__=="__main__":
    res = iterative_preorder_traversal(root)
    print(res)