from tree import Tree
import random

tree = Tree()
tree.addValue(2)
tree.addValue(5)
tree.addValue(7)
tree.addValue(6)
tree.addValue(21)

#print(tree.root.right.value)

for i in range(200000):
         tree.addValue( random.randint(0, 150000) )

print("\n"*2)

#print(tree.see())

while True:
         keywd = input("Número: ")
         if keywd == "":
                  break
         else:
                  tree.search(int(keywd))
