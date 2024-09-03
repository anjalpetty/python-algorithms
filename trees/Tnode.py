
class Tnode:
  def __init__(self, data=0, left=None, right=None):
    self.left: Tnode = left
    self.right: Tnode = right
    self.data: int = data
