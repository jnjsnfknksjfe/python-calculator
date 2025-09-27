
def calculator():
    print("Простий калькулятор на Python")
    print("Операції: +, -, *, /")
    
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Виберіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Помилка: ділення на нуль!"
        else:
            result = "Невідома операція!"
        
        print("Результат:", result)
    except ValueError:
        print("Помилка: потрібно вводити лише числа.")

if __name__ == "__main__":
    calculator()
