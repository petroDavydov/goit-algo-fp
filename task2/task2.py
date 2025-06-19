from turtle import Terminator
from tkinter import TclError  # use hint
import colorsys
import turtle
from colorama import Fore, Style, init
init(autoreset=True)


# use hint and google

def get_color_for_tree(depth, max_depth):
    hue = depth / max_depth
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

# Дерево піфагора з кутами, гілками використовуючи рекурсію


def tree_of_pifagor(t, depth, size, angle, max_depth):
    if depth <= 0 or size < 1:
        return
    t.pencolor(get_color_for_tree(depth, max_depth))

    t.right(angle)
    t.pencolor(get_color_for_tree(depth, max_depth))
    t.forward(size)
    tree_of_pifagor(t, depth - 1, size * 0.8, angle, max_depth)

    t.left(angle * 2)
    t.pencolor(get_color_for_tree(depth, max_depth))
    t.forward(size)
    tree_of_pifagor(t, depth - 1, size * 0.8, angle, max_depth)

    t.pencolor(get_color_for_tree(depth, max_depth))
    t.right(angle)
    tree_of_pifagor(t, depth - 1, size * 0.8, angle, max_depth)
    t.backward(size * 2)

# Виклик рекурсії та застосування параметрів малювання


def draw_tree_of_pifagor(depth):
    try:
        window = turtle.Screen()
        window.setup(width=900, height=800)
        window.bgcolor("white")

        size = 300 / (depth + 1)
        t = turtle.Turtle()
        t.speed(10)
        t.penup()
        t.goto(0, 163)
        t.left(90)
        t.forward(size)
        t.pendown()
        t.hideturtle()

        tree_of_pifagor(t, depth, size, angle=45, max_depth=depth)
        window.mainloop()
    except TclError:
        print(
            f"{Fore.LIGHTRED_EX}[❌] Ви закрили вікно вручну.[✔️] Ми прервали малювання!{Style.RESET_ALL}")
    except Terminator:
        print(
            f"{Fore.LIGHTRED_EX}[👉]Вікно закрито під час виконання коду, тобто малювання. Turtle зупинився.[💀]{Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        print(
            f"{Fore.CYAN}[😊] Спробуй побудувати фрактал --> <Дерево Піфагора>. Введи рівень рекурсії від 1 до 10.{Style.RESET_ALL}")
        user_input = input(
            f"{Fore.BLUE}Введіть рівень рекурсії: {Style.RESET_ALL}")
        user_input = int(user_input)
        if 0 < user_input <= 10:
            draw_tree_of_pifagor(user_input)
        else:
            print(
                f"{Fore.RED}[👉]Число має бути не менше 1 та не більше 10{Style.RESET_ALL}")
    except ValueError:
        print(
            f"{Fore.RED}[🔥]Ведіть ціле число. від 1 до 10. [🙏] Будь ласка{Style.RESET_ALL} ")
