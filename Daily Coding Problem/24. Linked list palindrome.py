class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None


def is_palindrome(node):
  tail = node
  while tail.next:
    tail = tail.next
  while node != tail:
    if node.val != tail.val:
      return False
    node = node.next
    tail = tail.prev
  return True


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))