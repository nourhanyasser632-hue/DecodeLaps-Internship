import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def add_expense():
    while True:
        expense = {
            "amount": int(input("Enter amount (0 to stop): ")),
            "category": input("Enter category: "),
            "date": input("Enter date: ")
        }

        if expense["amount"] == 0:
            break

        expenses.append(expense)
        save_expenses()


def list_expense():
    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses):
        print(
            i,
            "amount:", expense["amount"],
            "category:", expense["category"],
            "date:", expense["date"]
        )


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses:", total)


while True:
    option = int(input(
        "\nWelcome to Expense Tracker\n"
        "1. Add expenses\n"
        "2. View expenses\n"
        "3. View total\n"
        "4. Exit\n"
        "Choose an option: "
    ))

    if option == 1:
        add_expense()

    elif option == 2:
        list_expense()

    elif option == 3:
        total_expense()

    elif option == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option")