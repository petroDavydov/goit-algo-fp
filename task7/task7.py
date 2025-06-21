import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
init(autoreset=True)


def simulation_dice_roll(count_dice_role):
    sum_count = {i: 0 for i in range(2, 13)}

    dice1 = np.random.randint(1,6)
    dice2 = np.random.randint(1,6)
    result_diecs = dice1+dice2
    sum_count[result_diecs] +=1

    probabilities = {key: count / count_dice_role for key, count in sum_count.items()}

    probabilities_procent = {s: p * 100 for s,p in probabilities.items()}

    return probabilities_procent

def plot_probabilities(probabilities_procent):
    sums = list(probabilities_procent.keys())
    prob = list(probabilities_procent.values())

    plt.figure(figsize=(10, 8))
    plt.bar(sums, prob, color="lightgreen")
    plt.xlabel("SUMS")
    plt.ylabel("PROBABILITY")
    plt.xticks(sums)
    plt.yticks(prob)
    plt.grid(axis="both", linestyle="-*-", alfa=0.5)
    plt.show()

if __name__ == "__main__":

    user_input = input(print(f"{Fore.LIGHTMAGENTA_EX}Введіть кількість симуляцій: "))

    if user_input:
        print(f"{Fore.RED}Число 📛 НЕ має бути від'ємним! {Style.RESET_ALL}")
    
    probabilities_percent = simulation_dice_roll(user_input)

    print(f"{Fore.LIGHTWHITE_EX}Ймовірність суми у відсотках{Style.RESET_ALL}")

    for s, p in probabilities_percent.items():
        print(f"{Fore.LIGHTBLUE_EX}Сума -> {s}: {p:.2f} %")

    plot_probabilities(probabilities_percent)

    
