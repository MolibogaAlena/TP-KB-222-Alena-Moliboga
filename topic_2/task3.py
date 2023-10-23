def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка! Ділення на нуль неможливе."
    return x / y

def calculator(operation, x, y):
    match operation:
        case 'додавання':
            return add(x, y)
        case 'віднімання':
            return subtract(x, y)
        case 'множення':
            return multiply(x, y)
        case 'ділення':
            return divide(x, y)
        case _:
            return "Помилка: Невірна операція"

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

    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    operations = {
        '1': 'додавання',
        '2': 'віднімання',
        '3': 'множення',
        '4': 'ділення'
    }

    operation = operations.get(choice)
    result = calculator(operation, num1, num2)
    print("Результат:", result)
