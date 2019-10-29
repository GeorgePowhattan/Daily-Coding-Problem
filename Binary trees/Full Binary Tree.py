from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                #if any([not n.left and n.right, n.left and not n.right]):  # remove the nodes in which there is only 1 child
                #if any([ all([n.left is None, n.right is not None]),all([n.left is not None, n.right is None]) ]):
                if ((n.left and not n.right) or (not n.left and n.right)):
                    result += str(0)
                else:
                    result += str(n.value)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                num = num - 1
            if len(q):
                result += "\n"

        return result

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)

print(tree)
