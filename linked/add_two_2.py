
"""
Leetcode 2: Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional

from linked.LinkedList import *

# noinspection PyShadowingNames
def add_two_numbers(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:

  dummy = Node(-1)
  result = dummy
  carry = 0
  while l1 or l2:
    v1 = l1.data if l1 is not None else 0
    v2 = l2.data if l2 is not None else 0
    csum = v1 + v2 + carry
    if csum > 9:
      carry = csum // 10
      csum %= 10
    else:
      carry = 0
    result.next = Node(csum)
    result = result.next
    l1 = None if l1 is None else l1.next
    l2 = None if l2 is None else l2.next

  if carry > 0:
    result.next = Node(carry)
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

  l1, l2 = LinkedList(), LinkedList()

  l1.construct([2,4,3])
  l2.construct([5,6,4])
  res = add_two_numbers(l1.get_head(), l2.get_head())
  print_LL(res)

  l1.construct([9,9,9,9,9,9,9])
  l2.construct([9,9,9,9])

  res = add_two_numbers(l1.get_head(), l2.get_head())
  print_LL(res)
