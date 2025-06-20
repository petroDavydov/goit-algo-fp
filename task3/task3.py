import heapq
from colorama import Fore, Style, init
init(autoreset=True)


def dijkstra(graph, start):
    # Ініціалізація
    heap = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while heap:
        
        current_distance, current_vertex = heapq.heappop(heap)

        
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        
        for neighbor, weight in graph.get[current_vertex, []]:
                distance = current_distance + weight

            # При знаходжені короткого шляху
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

    return distances


def create_graph():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 3), ("D", 8)],
        "C": [("A", 3), ("B", 7), ("D", 3)],
        "D": [("B", 2), ("C", 1)],
        "E": [("G", 6), ("F", 4), ("A", 7)],
        "F": [("G", 1), ("E", 4)],
        "G": [("A", 9), ("F", 3), ("C", 1), ("E", 2)],
    }
    return graph


if __name__ == "__main__":
    print(f"{Fore.LIGHTWHITE_EX}Доступні вершини: {', '.join(create_graph().keys())}{Style.RESET_ALL}")
    graph = create_graph()
    user_input = input(
        f"{Fore.CYAN}Введіть вершину з якої почнемо досліджувати відстані: {Style.RESET_ALL}")
    if user_input:
        start_vertex = user_input.strip()

        if start_vertex not in graph:
            print(
                f"{Fore.RED}Вершини {start_vertex} в Графі не існує {Style.RESET_ALL}")
            exit()

        distances = dijkstra(graph, start_vertex)


        for vertex in distances:
            print(
                f"{Fore.MAGENTA}Відстань від {start_vertex} --> {vertex} === {Fore.LIGHTWHITE_EX}{distances[vertex]}{Style.RESET_ALL}")
