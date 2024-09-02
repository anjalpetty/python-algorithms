
"""
Leetcode: 21 Merge Two sorted lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Optional
from linked.LinkedList import Node, LinkedList


def merge_two_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
  dummy = Node(-1)
  curr = dummy
  while list1 and list2:
    if list1.data < list2.data:
      curr.next = list1
      list1 = list1.next
    else:
      curr.next = list2
      list2 = list2.next
    curr = curr.next

  if list1:
    curr.next = list1
  elif list2:
    curr.next = list2

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
  h1, h2 = LinkedList().construct([1,2,4]), LinkedList().construct([1,3,4])

  res = merge_two_lists(h1, h2)
  print("merged([1,2,4], [1,3,4]")
  print_LL(res)

  h1 = LinkedList().construct([])
  h2 = LinkedList().construct([])

  res = merge_two_lists(h1, h2)
  print("merged([], [])")
  print_LL(res)
