from colorama import Fore, Style, init
init(autoreset=True)


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(
                f"{Fore.LIGHTGREEN_EX}{item}: {info['cost']} money, {info['calories']} calories{Style.RESET_ALL}")
            total_cost += info["cost"]
            total_calories += info["calories"]
    return total_calories, total_cost, selected_items


def dynamic_programming(items, budget):
    # перетворюємо словник у пари
    item_list = list(items.items())
    numbers_of_items = len(item_list)
    # створення таблиці для максимальних калорій при бюджеті
    maximum_calories = [[0] * (budget + 1)
                        for _ in range(numbers_of_items + 1)]

    # заповнення таблиці
    for item_index in range(1, numbers_of_items + 1):
        name, info = item_list[item_index-1]
        cost, calories = info["cost"], info["calories"]
        for current_budget in range(budget + 1):
            if cost > current_budget:
                # якщо дорого відкидуємо
                maximum_calories[item_index][current_budget] = maximum_calories[item_index - 1][current_budget]
            else:
                # обираємо брати чи ні (максимум)
                maximum_calories[item_index][current_budget] = max(
                    maximum_calories[item_index - 1][current_budget], maximum_calories[item_index - 1][current_budget - cost] + calories)

    # Відновлення вибраних предметів
    selected_items = []
    current_budget = budget
    total_calories = maximum_calories[numbers_of_items][budget]
    total_cost = 0

    for item_index in range(numbers_of_items, 0, -1):
        name, info = item_list[item_index - 1]
        cost, calories = info["cost"], info["calories"]
        if total_calories <= 0:
            break  # виходимо
        if total_calories == maximum_calories[item_index - 1][current_budget]:
            continue  # не беремо продовжуємо обирати
        else:
            selected_items.append(
                f"{Fore.BLUE}{name} --> {Fore.LIGHTYELLOW_EX}{cost} money --> {Fore.LIGHTGREEN_EX}{calories} calories{Style.RESET_ALL} 👍")
            total_cost += cost
            total_calories -= calories
            current_budget -= cost

    return maximum_calories[numbers_of_items][budget], total_cost, selected_items


def screen_result(title, total_calories, total_cost, selecte_items):
    print(f"{Fore.LIGHTYELLOW_EX}\nВикористовуємо {title}{Style.RESET_ALL}")
    print(f"Що ми обрали з тестового набору:")
    for item in selecte_items:
        print(item)

    print(f"{Fore.RED}General calories: {total_calories} calories")
    print(f"{Fore.LIGHTBLACK_EX}General cost: {total_cost} money")


if __name__ == "__main__":

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    print(f"{Fore.CYAN}Спочатку відпрацьовують тестові дані! {Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}Тестовий набір:{Style.RESET_ALL}")

    for name, info in items.items():
        print(
            f"{name} --> {info['cost']} money --> {info['calories']} calories")

    budget = 100  # стандартний бюджет для тесту

    # greedy_algorithm
    greedy_calories, greedy_cost, greedy_items = greedy_algorithm(
        items, budget)
    screen_result("ЖАДІБНИЙ АЛГОРИТМ", greedy_calories,
                  greedy_cost, greedy_items)

    # dynamic_programming(dy_ming)
    dy_ming_calories, dy_ming_cost, dy_ming_items = dynamic_programming(
        items, budget)
    screen_result("ДИНАМІЧНЕ ПРОГРАМУВАННЯ", dy_ming_calories,
                  dy_ming_cost, dy_ming_items)
