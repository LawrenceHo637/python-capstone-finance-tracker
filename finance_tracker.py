# Custom error for receiving an empty string as input
class EmptyString(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


def add_expense(dictionary):
    try:
        description = input("Enter expense description: ")

        if description.replace(" ", "") == "":
            raise EmptyString("Invalid input! Description cannot be empty.\n")

        category = input("Enter category: ")

        if category.replace(" ", "") == "":
            raise EmptyString("Invalid input! Category cannot be empty.\n")

        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.\n")
    except EmptyString as e:
        print(e)
    else:
        dictionary[category] = (description, amount)
        print("Expense added successfully.\n")


def view_all_expenses(dictionary):
    for entry in dictionary:
        print(f"Category: {entry}")
        print(f"\t-{dictionary[entry][0]}: ${dictionary[entry][1]:.2f}")
    print("")


def view_summary(dictionary):
    print("Summary:")
    for entry in dictionary:
        print(f"{entry}: ${dictionary[entry][1]:.2f}")
    print("")


# The main function of the program, prompts user to select an action and calls corresponding function
def main():
    print("Welcome to the Personal Finance Tracker!")
    expenses = {}
    option = 0

    while option != 4:
        # Present user with the program menu and prompt for an option
        try:
            print("What would you like to do?")
            print("\t1. Add Expense")
            print("\t2. View All Expenses")
            print("\t3. View Summary")
            print("\t4. Exit")
            option = int(input("Choose an option [1, 2, 3, 4]: "))

            if option < 1 or option > 4:
                raise ValueError
        except ValueError:
            print("Invalid selection! Valid options are [1, 2, 3, 4].\n")
        else:
            if option == 1:
                add_expense(expenses)
            elif option == 2:
                view_all_expenses(expenses)
            elif option == 3:
                view_summary(expenses)
            else:
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()
