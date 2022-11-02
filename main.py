# Program make a simple calculator
"""Calculator's main.py"""
import calculations


def ask():
    """다시 계산할 건지 물어보는 function"""
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.upper() == "NO":
            ask_again = input("Are you sure? (yes/no): ")
            if ask_again.upper() == "YES":
                return 0
            else:
                return 1
        elif next_calculation.upper() == "YES":
            return 1
        else:
            continue


print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

filepath = "C:\\Users\\나맥2\\PycharmProjects\\ComplicatedCalc\\calc_log.txt"
f = open(filepath, 'a')

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", calculations.add(num1, num2))
            wtw = str(choice) + " : " + str(num1) + "+" + str(num2) + "=" + str(calculations.add(num1, num2)) + "\n"
            f.write(wtw)

        elif choice == '2':
            print(num1, "-", num2, "=", calculations.subtract(num1, num2))
            wtw = str(choice) + " : " + str(num1) + "-" + str(num2) + "=" + str(calculations.subtract(num1, num2)) + "\n"
            f.write(wtw)

        elif choice == '3':
            print(num1, "*", num2, "=", calculations.multiply(num1, num2))
            wtw = str(choice) + " : " + str(num1) + "*" + str(num2) + "=" + str(calculations.multiply(num1, num2)) + "\n"
            f.write(wtw)

        elif choice == '4':
            if num2 == 0:
                print("divide by zero err")
                wtw = str(choice) + " : " + str(num1) + "/" + str(num2) + "=" + "divide by zero err\n"
                f.write(wtw)

            else:
                print(num1, "/", num2, "=", calculations.divide(num1, num2))
                wtw = str(choice) + " : " + str(num1) + "/" + str(num2) + "=" + str(calculations.divide(num1, num2)) + "\n"
                f.write(wtw)

        # check if user wants another calculation
        # break the while loop if answer is no
        temp = ask()
        if temp == 0:
            break

    else:
        print("Invalid Input")
        wtw = choice + " : Invalid Input\n"
        f.write(wtw)

f.close()
