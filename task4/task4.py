import copy
import uuid
import heapq
from typing import Optional
import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
init(autoreset=True)


class Node:
    def __init__(self, key, color="skyblue"):
        self.left: Optional["Node"] = None  # виправлено для python аналізатора
        # виправлено для python аналізатора
        # виправлено для python аналізатора
        self.right: Optional["Node"] = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left = x - 1 / 2 ** layer
            pos[node.left.id] = (left, y - 1)
            left = add_edges(graph, node.left, pos, x=left,
                             y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right = x + 1 / 2 ** layer
            pos[node.right.id] = (right, y - 1)
            right = add_edges(graph, node.right, pos,
                              x=right, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# make heap desision
def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def build_binary_heap(heap, i=0):
    if i < len(heap):
        node = Node(heap[i])
        node.left = build_binary_heap(heap, 2 * i + 1)
        node.right = build_binary_heap(heap, 2 * i + 2)
        return node
    return None


if __name__ == "__main__":
    print(f"Спочатку виводимо {Fore.RED}Бінарне Дерево{Style.RESET_ALL}, \
а потім, {Fore.LIGHTGREEN_EX}за вашим вибором, СТВОРЮЄМО ДЕРЕВО З КУПИ!{Style.RESET_ALL} ")
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    draw_tree(root)

    # Вивід та побудова для купи з дерева
    heap_composition = {
        # приклад з великою і малою вагою
        "A": [90, 100, 113, 1, 55, 7, 8, 12345, 44],
        # середній розмір
        "B": [15, 10, 20, 5, 25],
        # збалансована купа
        "C": [1, 2, 3, 4, 5, 6, 7],
        # зменшення
        "D": [99, 87, 65, 43, 21, 10],
        # різнобій
        "E": [5, 17, 3, 22, 9, 50, 1, 2],
    }

    print(f"{Fore.LIGHTGREEN_EX}Ми маємо такі набори heap:{Style.RESET_ALL}")
    for key, value in heap_composition.items():
        print(
            f"{Fore.LIGHTBLUE_EX}{key} --> {Fore.LIGHTYELLOW_EX}{value}{Style.RESET_ALL}")

    user_input = input(
        f"{Fore.LIGHTRED_EX}Введіть букву обраної купи: {Style.RESET_ALL}").strip().upper()

    if user_input not in heap_composition:
        print(
            f"{Fore.RED}Нажаль обрати можна тільки з набору: A, B, C, D, E ⚠️{Style.RESET_ALL}")
    else:
        original_data_save = copy.deepcopy(heap_composition[user_input])
        heapq.heapify(original_data_save)
        root_heap = build_binary_heap(original_data_save)
        draw_heap(root_heap)
