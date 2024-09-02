"""
Leetcode: 23 Merge k Sorted lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
from typing import Optional, List
from linked.LinkedList import LinkedList, Node


# noinspection PyShadowingNames
def merge(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:

  if l1 is None and l2 is None:
    return None
  elif l1 is None and l2 is not None:
    return l2
  elif l1 is not None and l2 is None:
    return l1

  dummy = Node(-1)
  curr = dummy
  while l1 and l2:
    if l1.data < l2.data:
      curr.next = l1
      l1 = l1.next
    else:
      curr.next = l2
      l2 = l2.next
    curr = curr.next

  if l1:
    curr.next = l1
  if l2:
    curr.next = l2
  return dummy.next

def mergeK(lists: List[Optional[Node]], start: int, end: int) -> Optional[Node]:
  if start == end:
    return lists[start]

  mid = start + (end - start) // 2
  left_side = mergeK(lists, start, mid)
  right_side = mergeK(lists, mid+1, end)
  return merge(left_side, right_side)

def mergeKLists(lists: List[Optional[Node]]) -> Optional[Node]:

  if lists is None:
    return None

  return mergeK(lists, 0, len(lists)-1)

def print_LL(head: Optional[Node]):
  while head:
    if head.next is not None:
      print(head.data, end='->')
    else:
      print(head.data, end='')
    head = head.next
  print("")

if __name__ == '__main__':

  h1 = LinkedList().construct([1,4,5])
  h2 = LinkedList().construct([1,3,4])
  h3 = LinkedList().construct([2,6])
  h4 = LinkedList().construct([2,3])
  h5 = LinkedList().construct([5,6])

  res = mergeKLists([h1, h2, h3, h4, h5])
  print_LL(res)