
"""
Leetcode: 61 Rotate List

Given the head of a linked list, rotate the list to the right by k places
"""
from typing import Optional
from linked.LinkedList import Node, LinkedList


def rotate_right(head: Optional[Node], k: int) -> Optional[Node]:

  if not head:
    return head

  # find the length
  tail = head
  length = 1
  while tail.next:
    tail = tail.next
    length += 1

  k = k % length
  if k == 0:
    return head

  # move to the pivot point
  curr = head
  for i in range(length-k-1):
    curr = curr.next

  new_head = curr.next
  curr.next = None
  tail.next = head

  return new_head

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
  res = rotate_right(head, 2)
  print_LL(res)