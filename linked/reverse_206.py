"""
Leetcode: 206 Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional
from linked.LinkedList import LinkedList, Node


def reverse(head: Optional[Node]) -> Optional[Node]:
  if head is None or head.next is None:
    return head

  prev = None
  curr = head
  _next = None
  while curr:
    _next = curr.next
    curr.next = prev
    prev = curr
    curr = _next

  return prev

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
  res = reverse(head)
  print_LL(res)