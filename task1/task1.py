from typing import Optional  # use google
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
init(autoreset=True)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        if prev and cur:  # for python analyser
            prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self, label="Список"):
        print(f"{Fore.CYAN}\n{label}: ", end="")
        current = self.head
        while current:
            print(f"{Fore.GREEN}{current.data}", end=" --> ")
            current = current.next
        print(f"{Fore.RED}None{Style.RESET_ALL}")

    # reverse function

    def reverse_list(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        next_node = current.next
        current.next = None

        while next_node:
            temp = next_node.next
            next_node.next = current
            current = next_node
            next_node = temp
        self.head = current


    def sorted_insert(self, sorted_list, new_node):
        if not sorted_list.head or sorted_list.head.data >= new_node.data:
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            current = sorted_list.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sorted(self, linked_list):
        sorted_list = LinkedList()
        current = linked_list.head
        while current:
            next_node = current.next
            current.next = None
            self.sorted_insert(sorted_list, current)
            current = next_node
        linked_list.head = sorted_list.head

    def merge_sorted_list(self, list1, list2):
        cur = list1.head
        if not cur:
            list1.head = list2.head
            return list1

        while cur.next:
            cur = cur.next
        cur.next = list2.head
        list1.insertion_sorted(list1)
        return list1

    def plot(self, title="Список який виводимо на дісплей"):
        x, labels = [], []
        cur = self.head
        i = 0
        while cur:
            x.append(i)
            labels.append(cur.data)
            cur = cur.next
            i += 1

        plt.figure(figsize=(1.5 * len(x), 2.5))
        plt.scatter(x, [0] * len(x), s=800, color="lightgreen",
                    edgecolors="black", zorder=3)
        for i, label in enumerate(labels):
            plt.text(x[i], 0, str(label), fontsize=12, ha='center',
                     va='center', color='black', weight='bold')
        for i in range(len(x) - 1):
            plt.arrow(x[i], 0, 0.8, 0, head_width=0.05,
                      head_length=0.1, fc='black', ec='black', zorder=2)
        plt.axis('off')
        plt.title(title)
        plt.show()


# Створення списків
llist1 = LinkedList()
llist2 = LinkedList()

for value in [5, 15, 10]:
    llist1.insert_at_beginning(value)

for value in [20, 25, 11]:
    llist1.insert_at_end(value)

for value in [23, 18, 2, 38, 0, 43, 90]:
    llist2.insert_at_end(value)


# Друк початкових даних
llist1.print_list("Початковий Список №1")
llist2.print_list("Початковий Список №2")

# Візуалізація початкових
llist1.plot("Список №1 - до реверсу")
llist2.plot("Список №2 - до сортування")

# Реверс
llist1.reverse_list()
llist1.print_list("Список №1 після реверсу")
llist1.plot("Список №1 - після реверсу")

# Сортування
llist1.insertion_sorted(llist1)
llist2.insertion_sorted(llist2)
llist1.print_list("Список №1 після сортування")
llist2.print_list("Список №2 після сортування")

# Об’єднання списків та вивід
merged = LinkedList().merge_sorted_list(llist1, llist2)
merged.print_list("Об’єднаний відсортований список")
merged.plot("Об’єднаний список - графічно")
