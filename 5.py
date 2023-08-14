class Node:
  def __init__(self, val, l_node=None,r_node=None):
    self.val = val
    self.l_node = l_node
    self.r_node = r_node
    self.was = 0

node_0 = Node(3)
node_1 = Node(6)
node_2 = Node(5,node_0,node_1)
node_3 = Node(9)
node_4 = Node(11)
node_5 = Node(10,node_3,node_4)
node_tree = Node(8,node_2,node_5)

queue = [node_tree]

def go(x):
  print(x.val,end=' ')
  if x.l_node is not None:
      queue.append(x.l_node)
  if x.r_node is not None:
     queue.append(x.r_node)

while len(queue) !=0:
   go(queue[0])
   queue = queue[1:]
