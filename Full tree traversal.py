from collections import deque

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
   
    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)         # num vrstva je tu kvuli radkum str vypisu 
            while num > 0:
                n = q.popleft()
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

def fullBinaryTree(node):
    r = deque()
    r.append(node)
    result_full = ''
    while len(r):
        num = len(r)
        while num > 0:
            n = r.popleft()
                  
            if any([n.left and not n.right, not n.left and n.right]): #NEEED JUST ONE BRANCH
                result_full += str(0)
            else:
                result_full += str(n.value)
                r.append(n.left)
                r.append(n.right)
            num = num - 1
        if len(r):
            result_full += '\n'

    return result_full

print (fullBinaryTree(tree))