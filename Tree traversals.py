from collections import deque

class Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

# Breath-first traversal
#     1
#    / \
#   3   4
#  / \   \
# 2   5   7

# [1, 3, 4, 2, 5, 7]
def BFT(node):

    if node == None: return []

    queue = deque([node])
    output = []

    while len(queue)>0:

        current_node = queue.popleft()

        output.append(current_node.value)

        if current_node.left != None:
            queue.append(current_node.left) 

        if current_node.right != None:
            queue.append(current_node.right)

    return output


# Depth-first traversal = Pre-Order
#     1
#    / \
#   3   4
#  / \   \
# 2   5   7

# [1, 3, 2, 5, 4, 7]
res_DFT = []

def DFT(node):
    
    if node:
        
        res_DFT.append(node.value)    
        DFT(node.left)
        DFT(node.right)
    
    return res_DFT


# In-Order traversal
#     1
#    / \
#   3   4
#  / \   \
# 2   5   7

# [1, 3, 2, 5, 4, 7]
res_IO = []

def In_Order(node):
    
    if node:
        
        In_Order(node.left)
        res_IO.append(node.value)
        In_Order(node.right)
    
    return res_IO


# Post-Order traversal
#     1
#    / \
#   3   4
#  / \   \
# 2   5   7

# [1, 3, 2, 5, 4, 7]
res_PO = []

def Post_order(node):
    
    if node:
        
        Post_order(node.left)
        Post_order(node.right)
        res_PO.append(node.value)
    
    return res_PO


tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(DFT(tree))
print(BFT(tree))
print(In_Order(tree))
print(Post_order(tree))