import matplotlib.pyplot as plt
import heapq
from colorama import Fore, Style, init
init(autoreset=True)


def dijkstra(graph, start):
    # Ініціалізація
    heap = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()
    # для виводу візуалу use hint
    previous = {vertex: None for vertex in graph}

    while heap:

        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight

            # При знаходжені короткого шляху
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # для виводу візуалу use hint
                previous[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))

    return distances, previous


def create_graph():
    graph = {
        "A": [("B", 1), ("C", 4), ("D", 5), ("E", 7)],
        "B": [("A", 1), ("C", 3), ("D", 8), ("F", 6)],
        "C": [("A", 3), ("B", 7), ("D", 3), ("G", 1)],
        "D": [("A", 5), ("B", 2), ("C", 1), ("F", 4)],
        "E": [("A", 7), ("F", 4), ("G", 6), ("C", 5)],
        "F": [("B", 6), ("D", 4), ("E", 4), ("G", 2)],
        "G": [("C", 1), ("F", 2), ("E", 6), ("A", 9)],
    }

    return graph


# use from previous work(update for task 3)

def plot_path(path, title="Найкоротший шлях"):
    x = list(range(len(path)))
    y = [0.3] * len(x)

    plt.figure(figsize=(2.5 * len(x), 2.5))
    plt.scatter(x, y, s=800, color="lightgreen",
                edgecolors="black", zorder=3)

    for i, label in enumerate(path):
        plt.text(x[i], y[i], str(label), fontsize=12, ha='center',
                 va='center', color='black', weight='bold')

    for i in range(len(x) - 1):
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]],
                 color='black', linewidth=2, zorder=1)

    plt.axis('off')
    plt.title(title)
    plt.tight_layout()
    plt.show()

# для виводу візуалу по шляху use hint


def build_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    if path[0] == start:
        return path
    return


if __name__ == "__main__":
    graph = create_graph()
    print(f"{Fore.LIGHTWHITE_EX}Наявні вершини: {', '.join(graph.keys())}{Style.RESET_ALL}")

    start_user_input = input(
        f"{Fore.CYAN}Початкова вершина: {Style.RESET_ALL}").strip().upper()
    end_user_input = input(
        f"{Fore.YELLOW}Кінцева точка: {Style.RESET_ALL}").strip().upper()

    if start_user_input not in graph:
        print(
            f"{Fore.RED}Вершини {start_user_input} в графі не існує!{Style.RESET_ALL}")
        exit()
    if end_user_input not in graph:
        print(f"{Fore.RED}Вершини {end_user_input} в графі не існує!{Style.RESET_ALL}")
        exit()

    distances, previous = dijkstra(graph, start_user_input)

    print(
        f"\n{Fore.LIGHTCYAN_EX}Відстань від {start_user_input} вершини:{Style.RESET_ALL}")
    for vertex, distance in distances.items():
        print(
            f"{Fore.GREEN} ~ до -> {vertex}: {Fore.LIGHTWHITE_EX}{distance}{Style.RESET_ALL}")

    path = build_path(previous, start_user_input, end_user_input)

    if path:
        print(
            f"\n{Fore.LIGHTBLUE_EX}Шлях: -> {start_user_input} [👉] {end_user_input}:{Style.RESET_ALL} {' - - > '.join(path)}")
        plot_path(
            path, title=f"Шлях: -> {start_user_input} -->  {end_user_input}")
    else:
        print(
            f"{Fore.RED}❌ Немає шляху від {start_user_input} до {end_user_input}.{Style.RESET_ALL}")
