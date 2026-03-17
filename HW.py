# Калькулятор: просит два числа и оператор (+, -, *, /), выводит результат.
def calculator():
    user_input = input("Введите выражение (например, 5 + 3): ")

    try:
        parts = user_input.split()
        if len(parts) != 3:
            print("Неверный формат. Используйте: число оператор число")

        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])

        # Выполняем операцию
        if op == "+":
            result = sum(a, b)
        elif op == "-":
            result = minus(a, b)
        elif op == "*":
            result = umnozhenie(a, b)
        elif op == "/":
            if b == 0:
                print("Деление на ноль невозможно!")

            result = delele(a, b)
        else:
            print("Неизвестная операция. Используйте: +, -, *, /")

        print(f"Результат: {a} {op} {b} = {result}\n")

    except ValueError:
        print("Пожалуйста, введите корректные числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def sum(a, b):
    return a + b


def delele(a, b):
    return a / b


def minus(a, b):
    return a - b


def umnozhenie(a, b):
    return a * b


if __name__ == "__main__":
    calculator()
