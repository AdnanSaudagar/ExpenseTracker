import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create file with headers if not present
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
    except FileExistsError:
        pass

# Add an expense
def add_expense(category, amount):
    with open(FILE_NAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount])
    print("💰 Expense added successfully!\n")

# Display all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        print()
    except FileNotFoundError:
        print("⚠ No expense records found.\n")

# Show total spending
def total_expense():
    try:
        total = 0
        with open(FILE_NAME, "r") as file:
            next(file)  # Skip header
            for row in file:
                total += float(row.split(",")[2])
        print(f"📊 Total Expense: ₹{total}\n")
    except:
        print("⚠ No records to calculate.\n")

# Main menu
def menu():
    initialize_file()
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expense")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(category, amount)
        
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("👍 Thank you for using Expense Tracker!")
            break
        else:
            print("❌ Invalid option! Try again.\n")

if __name__ == "__main__":
    menu()
