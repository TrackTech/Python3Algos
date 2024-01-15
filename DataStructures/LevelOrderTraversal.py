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


def level_order_traversal(node):
    from collections import deque
    if not node:
        return None
    result = []

    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

if __name__=="__main__":
    res = level_order_traversal(root)
    print(res)
