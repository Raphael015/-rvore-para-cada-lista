class Node:
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None

class BinaryTree:
  def __init__(self):
      self.root = None

  def insert(self, key):
      self.root = self._insert(self.root, key)

  def _insert(self, root, key):
      if root is None:
          return Node(key)
      if key < root.key:
          root.left = self._insert(root.left, key)
      else:
          root.right = self._insert(root.right, key)
      return root

  def delete(self, key):
      self.root = self._delete(self.root, key)

  def _delete(self, root, key):
      if root is None:
          return root

      if key < root.key:
          root.left = self._delete(root.left, key)
      elif key > root.key:
          root.right = self._delete(root.right, key)
      else:
          if root.left is None:
              return root.right
          elif root.right is None:
              return root.left

          root.key = self._find_min(root.right).key
          root.right = self._delete(root.right, root.key)

      return root

  def _find_min(self, root):
      current = root
      while current.left is not None:
          current = current.left
      return current

  def inorder_traversal(self, root, result):
      if root:
          self.inorder_traversal(root.left, result)
          result.append(root.key)
          self.inorder_traversal(root.right, result)

# Lista1
lista1 = [45, 20, 30, 60, 81, 97, 100, 7, 8, 4]
tree1 = BinaryTree()
for item in lista1:
  tree1.insert(item)

print("Árvore antes da remoção:")
result1_before = []
tree1.inorder_traversal(tree1.root, result1_before)
print(result1_before)

# Adiciona um valor à árvore1
tree1.insert(55)

# Remove um valor da árvore1 (pode ser um nó com dois filhos)
tree1.delete(60)

print("\nÁrvore após adição e remoção:")
result1_after = []
tree1.inorder_traversal(tree1.root, result1_after)
print(result1_after)

# Lista2
lista2 = [15, 6, 18, 3, 7, 16, 20, 4]
tree2 = BinaryTree()
for item in lista2:
  tree2.insert(item)

print("\nÁrvore antes da remoção:")
result2_before = []
tree2.inorder_traversal(tree2.root, result2_before)
print(result2_before)

# Adiciona um valor à árvore2
tree2.insert(10)

# Remove um valor da árvore2 (nó sem dois filhos)
tree2.delete(15)

print("\nÁrvore após adição e remoção:")
result2_after = []
tree2.inorder_traversal(tree2.root, result2_after)
print(result2_after)
