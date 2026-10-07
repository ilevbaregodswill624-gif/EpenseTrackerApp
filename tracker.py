import sqlite3

def add_expense():
    description = input("What did you spend money on?")
    amount = float(input("How much did you spend?"))
    category = input("What category?")
    date = input("Date (YYYY-MM-DD)")

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
           CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                amount REAL,
                category TEXT,
                date TEXT
                )
            """)

    cursor.execute("""
      INSERT INTO expenses (description, amount, category, date)
      VALUES(?,?,?,?)
      """,(description, amount, category, date))

    connection.commit()
    connection.close()

    print("Expense saved successfully!")

def view_expenses():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
               CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT,
                    amount REAL,
                    category TEXT,
                    date TEXT
                    )
                """)

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    for expense in expenses:
        print("ID:", expense[0])
        print("Description:", expense[1])
        print("Amount: $", expense[2])
        print("Category:", expense[3])
        print("Date:", expense[4])

    connection.close()

print("=== EXPENSE TRACKER ===")
print("1. Add Expense")
print("2. View Expenses")
print("3. Exit")

choice = input("Choose an option: ")

if choice == "1":
    add_expense()
elif choice == "2":
    view_expenses()
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid option.")
