from colorama import Fore, Style, init
init(autoreset=True)


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    total_calories = 0
    total_cost = 0


    for item, info in sorted_items:
        if total_cost + info["cost"] <=budget:
            selected_items.append(f"{Fore.LIGHTGREEN_EX}{item}: {info['cost']} money, {info['calories']} calories{Style.RESET_ALL}")
            total_cost+=info["cost"]
            total_calories+=info["calories"]
    return total_calories, total_cost,selected_items

def screen_result(title, total_calories, total_cost, selecte_items):
    print(f"{Fore.LIGHTYELLOW_EX}\nTitle: {title}{Style.RESET_ALL}")
    for item in selecte_items:
        print(f"What we have: {item}")
    print(f"{Fore.RED}General calories: {total_calories} calories")
    print(f"{Fore.LIGHTBLACK_EX}General cost: {total_cost} money")


def dynamic_programming(items, budget):
    item_list = list(items.items())
    N = len(item_list)
    dp = [[0] * (budget+ 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        name, info = item_list[i-1]
        cost, calories = info["cost"], info["calories"]
        for w in range(budget + 1):
            if cost > w:
                dp[i][w] = dp[i - 1][w]  
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)

    return dp[N][budget]


  


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


