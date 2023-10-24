def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Помилка! Ділення на нуль неможливе."
    return result

while True:
    print("Зробіть вибір операції:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    choice = input("Введіть номер операції (1/2/3/4/5): ")

    if choice == '5':
        print("Вихід")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Помилка: Неправильний вибір")
        continue

    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: Введено некоректні дані.")
        continue

    if choice == '1':
        print("Результат:", add(num1, num2))
    elif choice == '2':
        print("Результат:", subtract(num1, num2))
    elif choice == '3':
        print("Результат:", multiply(num1, num2))
    elif choice == '4':
        print("Результат:", divide(num1, num2))

    next_operation = input("Введіть 'так' для нової операції або 'ні' для виходу: ")
    if next_operation.lower() != 'так':
        break
