# Create a Node class to create a node


class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Create a LinkedList class
class LinkedList:

  def __init__(self):
    self.head = None

  def get_head(self):
    return self.head

  # Method to add a node at begin of LL
  def insert_at_begin(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    else:
      new_node.next = self.head
      self.head = new_node

  # construct a linked list from array of numbers
  def construct(self, nums):
    self.head = None # this is to create new list from scratch every time construct is called
    curr = None
    for n in nums:
      if self.head is None:
        self.head = Node(n)
        curr = self.head
        continue
      else:
        curr.next = Node(n)
        curr = curr.next
    return self.head

  # Method to add a node at any index
  # Indexing starts from 0.
  def insert_at_index(self, data, index):
    if index == 0:
      self.insert_at_begin(data)

    position = 0
    curr = self.head
    while curr is not None and position+1 != index:
      position = position+1
      curr = curr.next

    if curr is not None:
      new_node = Node(data)
      new_node.next = curr.next
      curr.next = new_node
    else:
      print("Index not present")

  # Method to add a node at the end of LL
  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    curr = self.head
    while curr.next:
      curr = curr.next

    curr.next = new_node

  # Update node of a linked list
  # at given position
  def update_node(self, val, index):
    curr = self.head
    position = 0
    if position == index:
      curr.data = val
    else:
      while curr is not None and position != index:
        position = position+1
        curr = curr.next

      if curr is not None:
        curr.data = val
      else:
        print("Index not present")

  # Method to remove first node of linked list

  def remove_first_node(self):
    if self.head is None:
      return

    self.head = self.head.next

  # Method to remove last node of linked list
  def remove_last_node(self):

    if self.head is None:
      return

    curr = self.head
    while curr is not None and curr.next.next is not None:
      curr = curr.next

    curr.next = None

  # Method to remove at given index
  def remove_at_index(self, index):
    if self.head is None:
      return

    curr = self.head
    position = 0
    if position == index:
      self.remove_first_node()
    else:
      while curr is not None and position+1 != index:
        position = position+1
        curr = curr.next

      if curr is not None:
        curr.next = curr.next.next
      else:
        print("Index not present")

  # Method to remove a node from linked list
  def remove_node(self, data):
    curr = self.head

    if curr.data == data:
      self.remove_first_node()
      return

    while curr is not None and curr.next.data != data:
      curr = curr.next

    if curr is None:
      return
    else:
      curr.next = curr.next.next

  # Print the size of linked list
  def size_of_LL(self):
    size = 0
    if self.head:
      curr = self.head
      while curr:
        size = size+1
        curr = curr.next
      return size
    else:
      return 0

  # print method for the linked list
  def print_LL(self):
    curr = self.head
    while curr:
      if curr.next is not None:
        print(curr.data, end='->')
      else:
        print(curr.data, end='')
      curr = curr.next
    print("")

  # print method for the linked list
  def print_LL(self, ):
    curr = self.head
    while curr:
      if curr.next is not None:
        print(curr.data, end='->')
      else:
        print(curr.data, end='')
      curr = curr.next
    print("")

if __name__ == '__main__':
  # create a new linked list
  llist = LinkedList()

  # add nodes to the linked list
  llist.insert_at_end(1)
  llist.insert_at_end(2)
  llist.insert_at_begin(3)
  llist.insert_at_end(4)
  llist.insert_at_index(0, 2)

  # print the linked list
  print("Node Data")
  llist.print_LL()

  # remove a nodes from the linked list
  print("\nRemove First Node")
  llist.remove_first_node()
  print("Remove Last Node")
  llist.remove_last_node()
  print("Remove Node at Index 1")
  llist.remove_at_index(1)

  # print the linked list again
  print("\nLinked list after removing a node:")
  llist.print_LL()

  print("\nUpdate node Value")
  llist.update_node('z', 0)
  llist.print_LL()

  print("\nSize of linked list :", end=" ")
  print(llist.size_of_LL())