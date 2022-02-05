from mx.utils.LinkedListNode import LinkedListNode


class LinkedList:

   def __init__(self):
      super().__init__()
      self._head = LinkedListNode()
      self._tail = LinkedListNode()
      self._head.next = self._tail
      self._tail.prev = self._head
      self._length:float = 0

   @property
   def head(self) -> LinkedListNode:
      return None if self._head.next == self._tail else self._head.next

   @property
   def length(self) -> float:
      return self._length

   @property
   def tail(self) -> LinkedListNode:
      return None if self._tail.prev == self._head else self._tail.prev

   def insertAfter(self, value, prev:LinkedListNode) -> LinkedListNode:
      node:LinkedListNode = self.makeNode(value)
      node.prev = prev
      node.next = prev.next
      node.prev.next = node
      node.next.prev = node
      self._length += 1
      return node

   def insertBefore(self, value, next:LinkedListNode) -> LinkedListNode:
      node:LinkedListNode = self.makeNode(value)
      node.prev = next.prev
      node.next = next
      node.prev.next = node
      node.next.prev = node
      self._length += 1
      return node

   def find(self, value) -> LinkedListNode:
      cur:LinkedListNode = self._head
      while cur.value != value and cur != self._tail:
         cur = cur.next
      return None if cur == self._tail else cur

   def remove(self, value) -> LinkedListNode:
      node:LinkedListNode = self.getNode(value)
      if node:
         node.prev.next = node.next
         node.next.prev = node.prev
         node.next = node.prev = None
         self._length -= 1
      return node

   def append(self, value) -> LinkedListNode:
      return self.insertAfter(value, self._tail.prev)

   def pop(self) -> LinkedListNode:
      return None if self._length == 0 else self.remove(self._tail.prev)

   def unshift(self, value) -> LinkedListNode:
      return self.insertAfter(value, self._head)

   def shift(self) -> LinkedListNode:
      return None if self._length == 0 else self.remove(self._head.next)

   def getNode(self, value) -> LinkedListNode:
      return value if isinstance(value, LinkedListNode) else self.find(value)

   def makeNode(self, value) -> LinkedListNode:
      return value if isinstance(value, LinkedListNode) else LinkedListNode(value)
