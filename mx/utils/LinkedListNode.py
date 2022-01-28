from typing import Any


class LinkedListNode:
   
   next:'LinkedListNode'
   
   prev:'LinkedListNode'
   
   value:Any
   
   def __init__(self, value = None):
      super().__init__()
      self.value = value
   