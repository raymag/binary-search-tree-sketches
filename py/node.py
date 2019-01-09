class Node():
         def __init__(self, value):
                  self.value = value
                  self.left = None
                  self.right = None
                  
         def addNode(self, node):
                  if node.value < self.value:
                           if self.left == None:
                                    self.left = node
                           else:
                                    self.left.addNode(node)
                  elif node.value > self.value:
                           if self.right == None:
                                    self.right = node
                           else:
                                    self.right.addNode(node)
                                    
         def search(self, value):
                  if self.value > value:
                           if self.left != None:
                                    self.left.search(value)
                           else:
                                    print(value, " não encontrado!")
                  elif self.value < value:
                           if self.right != None:
                                    self.right.search(value)
                           else:
                                    print(value, " não encontrado!")
                  else:
                           print(value, "encontrado!")

#         def listify(self, nodes):
#                 if self.left != None:
#                           self.left.listify(nodes)
#                  nodes.append(self.value)
#                 if self.right != None:
#                           self.right.listify(nodes)
#                  return nodes

         def visit(self):
                  if self.left != None:
                           self.left.visit()
                  print(self.value)
                  if self.right != None:
                           self.right.visit()
