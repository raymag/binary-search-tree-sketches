from node import Node

class Tree():
         def __init__(self):
                  self.root = None
                  
         def addValue(self, value):
                  if self.root == None:
                           self.root =  Node(value)
                  else:
                           self.root.addNode(Node(value))
                           
         def search(self, value):
                  self.root.search(value)

         def see(self):
                  self.root.visit()

         #def listify(self):
         #        return self.root.listify(nodes=[])
