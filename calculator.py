num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter your choice: "))

if choice > 5 or choice <= 0:
    print("Please! Enter the choice from (1-5)")
else:
    if choice == 1:
        print(f"The addition of {num1} and {num2} is: {num1 + num2}")
    elif choice == 2:
        print(f"The subtraction of {num1} and {num2} is: {num1 - num2}")
    elif choice == 3:
        print(f"The multiplication of {num1} and {num2} is: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"The division of {num1} and {num2} is: {num1 / num2}")
        else:
            print("Error! Division by zero is not allowed.")
    elif choice == 5:
        print(f"The modulus of {num1} and {num2} is: {num1 % num2}")