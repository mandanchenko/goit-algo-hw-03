import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_flake(t, order, size):
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)


def main():
    # Введення рівня рекурсії від користувача
    order = int(input("Введіть рівень рекурсії (ціле число): "))

    # Створення вікна та налаштування
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Сніжинка Коха")

    # Створення черепашки та налаштування
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-50, -50)
    t.pendown()

    # Виклик функції для малювання сніжинки Коха
    draw_koch_flake(t, order, 100)

    # Завершення програми при кліку на вікно
    screen.exitonclick()


if __name__ == "__main__":
    main()
