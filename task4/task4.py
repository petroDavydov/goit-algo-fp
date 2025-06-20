import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      left = x - 1 / 2 ** layer
      pos[node.left.id] = (left, y - 1)
      left = add_edges(graph, node.left, pos, x=left, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      right = x + 1 / 2 ** layer
      pos[node.right.id] = (right, y - 1)
      right = add_edges(graph, node.right, pos, x=right, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

# make heap desision
def draw_heap(heap_root):
  heap = nx.DiGraph()
  pos = {heap_root.id: (0, 0)}
  heap = add_edges(heap, heap_root, pos)

  colors = [node[1]['color'] for node in heap.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


def buil_binary_heap(heap, i):
  if i<Node(heap):
    node = Node(heap(i))
    node.left = buil_binary_heap(heap, 2 * i + 1)
    node.right = buil_binary_heap(heap, 2 * i + 2)
    return node
  
if __name__ == "__main__":  
# Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    draw_tree(root)

    numbers_heap = [90, 100, 113,1,55,7,8,12345,44]
    heapq.heapify(numbers_heap)
    root_heap= buil_binary_heap(numbers_heap)

    draw_heap(root_heap)

