import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
init(autoreset=True)

# Функція симуляції кидання


def simulation_dice_roll(count_dice_role):
    sum_count = {i: 0 for i in range(2, 13)}

    # симуляція кидків кубіка
    for _ in range(count_dice_role):
        dice1 = np.random.randint(1, 7)  # генерація числа першого кубіка
        dice2 = np.random.randint(1, 7)  # генерація числа другого кубіка
        result_diecs = dice1+dice2  # сума кубіків
        sum_count[result_diecs] += 1  # для отримання суми

    probabilities = {key: count / count_dice_role for key,
                     count in sum_count.items()}  # перетворення у ймовірності
    # конвертація у відсотки
    probabilities_procent = {s: p * 100 for s, p in probabilities.items()}

    return probabilities_procent, sum_count  # додано sum_count для розрахунуків

# Для побудови графіка


def plot_probabilities(probabilities_procent):
    sums = list(probabilities_procent.keys())  # отримуємо список ключів-сум
    # отримуємо список ймовірностей-значень у %
    prob = list(probabilities_procent.values())

    plt.figure(figsize=(10, 8))
    plt.title("Probability of Each Sum")
    plt.bar(sums, prob, color="lightgreen")
    plt.xlabel("SUM")
    plt.ylabel("PROBABILITY (%)")
    plt.xticks(sums)
    # змінено для уникнення помилок, було plt.ystics(prob)
    plt.yticks(np.arange(0, max(prob) + 1, step=2))
    plt.grid(axis="y", linestyle="-", alpha=0.5)
    plt.show()


if __name__ == "__main__":

    user_input = input(f"{Fore.LIGHTMAGENTA_EX}Введіть кількість симуляцій: ")

    try:
        count_dice_role = int(user_input)
        if count_dice_role <= 0:
            print(f"{Fore.RED}Число 📛 НЕ має бути від'ємним! {Style.RESET_ALL}")
            exit()
    except ValueError:
        print(f"{Fore.LIGHTRED_EX}Введіть ціле цісло!{Style.RESET_ALL}")
        exit()

    probabilities_percent, sum_count = simulation_dice_roll(count_dice_role)

   # Наявні аналітичні ймовірності
    theoretical_probabilities = {
        2: "2.78% (1/36)", 3: "5.56% (2/36)", 4: "8.33% (3/36)", 5: "11.11% (4/36)",
        6: "13.89% (5/36)", 7: "16.67% (6/36)", 8: "13.89% (5/36)", 9: "11.11% (4/36)",
        10: "8.33% (3/36)", 11: "5.56% (2/36)", 12: "2.78% (1/36)"
    }

    # Табличний вивід
    print(f"\n{Fore.LIGHTWHITE_EX}{Style.BRIGHT}{'Сума':^6} | {'Ймовірність (Метод Монте-Карло)':^30} | {'Ймовірність (Аналітична)':^20} | {'Відхилення (%)':^14}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}{Style.BRIGHT}{'-'*6} | {'-'*30} | {'-'*20} | {'-'*14}{Style.RESET_ALL}")

    for s in range(2, 13):
        monte_carlo_prob = probabilities_percent[s]
        theoretical_prob = float(theoretical_probabilities[s].split("%")[0])
        deviation = monte_carlo_prob - theoretical_prob
        deviation_sign = "+" if deviation >= 0 else "-"

        monte_carlo_str = f"{monte_carlo_prob:.2f}% ({sum_count[s]}/{count_dice_role})"
        theoretical_str = f"{theoretical_prob:.2f}%"
        deviation_str = f"{deviation_sign}{abs(deviation):.2f}%"

        print(f"{Fore.LIGHTBLUE_EX}{s:^6}{Style.RESET_ALL} | {monte_carlo_str:^30} | {theoretical_str:^20} | {deviation_str:^14}")

    plot_probabilities(probabilities_percent)
