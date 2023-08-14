class Node:
  def __init__(self, value, l_node=None,r_node=None):
    self.value = value
    self.l_node = l_node
    self.r_node = r_node

node_0 = Node(3)
node_1 = Node(6)
node_2 = Node(5,node_0,node_1)
node_3 = Node(9)
node_4 = Node(11)
node_5 = Node(10,node_3,node_4)
node_tree = Node(8,node_2,node_5)

def print_tree(x:Node):
  if x.l_node is not None:
      print_tree(x.l_node)
  print(x.value, end = ' ')
  if x.r_node is not None:
     print_tree(x.r_node)

print_tree(node_tree)