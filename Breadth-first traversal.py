from collections import deque

class Node:

       def __init__(self,info):

           self.info = info
           self.left = None
           self.right = None
           self.level = None

       def __str__(self):

           return str(self.info)

def BFT(node):

    node.level = 1
    queue = deque([node])
    output = []
    current_level = node.level

    while len(queue)>0:

          current_node = queue.popleft()

          if(current_node.level > current_level):
              output.append("\n")
              current_level += 1

          output.append(str(current_node))

          if current_node.left != None:
             current_node.left.level = current_level + 1 
             queue.append(current_node.left) 

          if current_node.right != None:
             current_node.right.level = current_level + 1 
             queue.append(current_node.right)

    return ''.join(output)

root = Node(9)
root.left = Node(2)
root.right = Node(4)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(5)
root.right.right = Node(7)

print(BFT(root))



-------------------------------------------------------------------------------------
### Shorter variant without levels:
from collections import deque

class Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value


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

root = Node(9)
root.left = Node(2)
root.right = Node(4)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(5)
root.right.right = Node(7)

print(BFT(root))