class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculator(self):
        while True:
            wish = input("Do you need to do calculations? If yes, type 'yes'; otherwise, type 'no': ").strip().lower()
            if wish == 'no':
                print("Ok! Bye")
                break
            elif wish == 'yes':
                while True:
                    print("Let's start calculations")
                    print("Enter your choice:")
                    print("1. Addition")
                    print("2. Subtraction")
                    print("3. Multiplication")
                    print("4. Division")
                    print("5. Modulo Division")
                    print("6. Exit")

                    try:
                        choice = int(input("Your choice: "))
                        if choice == 1:
                            print("ADD =", self.num1 + self.num2)
                        elif choice == 2:
                            print("SUB =", self.num1 - self.num2)
                        elif choice == 3:
                            print("MUL =", self.num1 * self.num2)
                        elif choice == 4:
                            if self.num2 != 0:
                                print("DIV =", self.num1 / self.num2)
                            else:
                                print("Cannot divide by zero.")
                        elif choice == 5:
                            print("MODULO DIV =", self.num1 % self.num2)
                        elif choice == 6:
                            print("Exiting calculator.")
                            return
                        else:
                            print("INVALID CHOICE. Please try again.")
                    except ValueError:
                        print("Please enter a valid number for choice.")
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        obj = Calculator(num1, num2)
        obj.calculator()
    except ValueError:
        print("Invalid input. Please enter valid integers.")
