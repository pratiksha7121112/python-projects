import csv

transactions = []

def show_menu():
    print("BUDGET TRACKER")
    print("")
    print("")
    print("MENU")
    print("")
    print("1. Add income")
    print("")
    print("2. Add expense")
    print("")
    print("3. View balance")
    print("")
    print("4. View Transaction history")
    print("")
    print("5. Save to CSV")
    print("")
    print("6. Exit")
    print("")

def add_income():
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    transactions.append({"type": "income", "description": description, "amount": amount})
    print("Income added!")

def add_expense():
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    transactions.append({"type": "expense", "description": description, "amount": amount})
    print("Expense added!")

def view_balance():
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        elif transaction["type"] == "expense":
            total_expenses += transaction["amount"]
    print("Total income:", total_income)
    print("Total expenses:", total_expenses)
    print("Balance:", total_income - total_expenses)

def view_history():
        if not transactions:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction["type"].upper(), "|", transaction["description"], "|", transaction["amount"])
    
def save_to_csv():
    with open("budget.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Description", "Amount"])
        for transaction in transactions:
            writer.writerow([transaction["type"], transaction["description"], transaction["amount"]])
    print("Saved to budget.csv!")

while True:
    show_menu()
    choice = input("Select an option: ")
    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_balance()
    elif choice == "4":
        view_history()
    elif choice == "5":
        save_to_csv()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")