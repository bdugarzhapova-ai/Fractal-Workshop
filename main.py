import turtle
from fractals import basic, koch, complex


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Fractal Workshop")
    turtle.speed(0)

    while True:
        turtle.reset()
        turtle.speed(0)

        print("\n" + "=" * 30)
        print("      ГЛАВНОЕ МЕНЮ")
        print("=" * 30)
        print("1. Бинарное дерево")
        print("2. Ветка")
        print("3. Кох")
        print("4. Снежинка Коха")
        print("5. Минковский")
        print("6. Ледяной фрактал 1")
        print("7. Ледяной фрактал 2")
        print("8. Леви")
        print("9. Выход")
        print("=" * 30)

        choice = input("Выберите фрактал (1-9): ")

        if choice == '9':
            print("Выход из программы.")
            break

        try:
            if choice == '1':
                order = int(input("Порядок: "))
                size = int(input("Размер: "))
                angle = int(input("Угол: "))

                turtle.up()
                turtle.setheading(90)
                turtle.down()

                basic.draw_binary_tree(order, size, angle)
            elif choice == '2':
                order = int(input("Порядок: "))
                size = int(input("Размер: "))

                turtle.up()
                turtle.setheading(90)
                turtle.down()

                basic.draw(size, order)
                turtle.up()
            elif choice == '3':
                koch.koch(int(input("Порядок: ")), int(input("Размер: ")))
            elif choice == '4':
                koch.koch_snowflake(int(input("Порядок: ")), int(input("Размер: ")))
            elif choice == '5':
                koch.minkowski(int(input("Порядок: ")), int(input("Размер: ")))
            elif choice == '6':
                complex.ice_fractal_1(int(input("Порядок: ")), int(input("Размер: ")))
            elif choice == '7':
                complex.ice_fractal_2(int(input("Порядок: ")), int(input("Размер: ")))
            elif choice == '8':
                complex.levy(int(input("Порядок: ")), int(input("Размер: ")))

            else:
                print("Неверный выбор.")
        except ValueError:
            print("Ошибка: вводите только числа")


if __name__ == "__main__":
    main()