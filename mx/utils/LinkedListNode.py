from typing import Any

class LinkedListNode:

   next:'LinkedListNode'

   prev:'LinkedListNode'

   value:Any

   def __init__(self, value = None):
      self.value = value
      self.next = None
      self.prev = None
