"""
Leetcode 19: Remove nth node from end
"""

from typing import Optional
from linked.LinkedList import *

def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
  dummy = Node(-1, head)
  start = dummy
  end = head

  # move pointer to nth position from begining
  while n > 0 and end:
    end = end.next
    n -= 1

  # iterate start and end till end reaches null
  while end:
    start = start.next
    end = end.next

  # delete the nth node from end
  start.next = start.next.next
  return dummy.next

def print_LL(head: Optional[Node]):
  while head:
    if head.next is not None:
      print(head.data, end='->')
    else:
      print(head.data, end='')
    head = head.next
  print("")

if __name__ == '__main__':

  head = LinkedList().construct([1,2,3,4,5])

  res = remove_nth_from_end(head, 2)
  print_LL(res)

  head = LinkedList().construct([1,2])
  res = remove_nth_from_end(head, 1)
  print_LL(res)